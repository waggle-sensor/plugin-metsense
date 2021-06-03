import argparse
from pathlib import Path
import time
import logging
import sys
import waggle.plugin as plugin


def find_device_path(name):
    for path in Path("/sys/bus/iio/devices").glob("*/name"):
        if path.read_text().strip() == name:
            return path.parent
    raise FileNotFoundError(f"unable to find path for device {name}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="enable debug logs")
    parser.add_argument("--name", default="bme680", type=str, help="name of iio device to use")
    parser.add_argument("--rate", default=30.0, type=float, help="sampling rate")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format="%(asctime)s %(message)s",
                        datefmt="%Y/%m/%d %H:%M:%S")

    try:
        device_path = find_device_path(args.name)
    except FileNotFoundError:
        logging.error("no iio device found for %s", args.name)
        sys.exit(1)

    plugin.init()

    meta = {"sensor": args.name}

    while True:
        time.sleep(args.rate)
        for path in device_path.glob("in_*_input"):
            key = path.name
            value = float(path.read_text())
            plugin.publish(f"iio.{key}", meta=meta)

if __name__ == "__main__":
    main()
