import argparse
from busio import I2C
import adafruit_bme680
import time
import board
import logging
import waggle.plugin as plugin

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="enable debug logs")
    parser.add_argument("--address", default=0x76, type=int, help="i2c address to use")
    parser.add_argument("--rate", default=3.0, type=float, help="sampling rate")
    parser.add_argument("--sea-level-pressure", default=1013.25, type=float, help="sea level pressure at sensor location")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO,
                        format="%(asctime)s %(message)s",
                        datefmt="%Y/%m/%d %H:%M:%S")

    plugin.init()

    logging.info("setting up i2c interface")
    i2c = I2C(board.SCL, board.SDA)

    logging.info("setting up BME280 sensor")
    bme680 = adafruit_bme680.Adafruit_BME680_I2C(i2c, address=args.address)

    # change this to match the location's pressure (hPa) at sea level
    logging.info("setting sea level pressure to %0.1f", args.sea_level_pressure)
    bme680.sea_level_pressure = args.sea_level_pressure

    while True:
        logging.info("Temperature %0.1f C, Gas %0.1f count, Humidity %0.1f %%RH, Pressure %0.1f hPa, Altitude %0.1f m",
            bme680.temperature,
            bme680.gas,
            bme680.relative_humidity,
            bme680.pressure,
            bme680.altitude)

        plugin.publish("env.temperature.bme280", bme680.temperature)
        plugin.publish("env.relative_humidity.bme280", bme680.relative_humidity)
        plugin.publish("env.pressure.bme280", bme680.pressure)
        plugin.publish("env.altitude.bme280", bme680.altitude)

        time.sleep(args.rate)

if __name__ == "__main__":
    main()
