# Metsense Plugin

This plugin works with the [BME680](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme680/) sensor to provide basic meteorological data.

Note: The plugin expects the BME680 sensor to have address 0x76 (configurable) and can have its sea level pressure set based on the node's location for most accurate readings.

Note: This plugin requires privileged access to the host system to work with the I2C bus and to detect the platform using /proc. This currently *only* works on the Raspberry Pi due to how the GPIO dependencies attempts to detect the platform.
