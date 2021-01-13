# Metsense Plugin

This plugin works with the [BME280](https://www.bosch-sensortec.com/products/environmental-sensors/humidity-sensors-bme280/) sensor to provide basic meteorological data.

Note: This plugin requires access to the I2C bus on the device, expects the BME280 to have address 0x76 (configurable) and can / needs to have its sea level pressure at the node's location specified.
