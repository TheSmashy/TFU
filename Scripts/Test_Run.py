#!/usr/bin/python3
import time
from datetime import datetime
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280
import adafruit_tsl2591
from w1thermsensor import W1ThermSensor
from influxdb import InfluxDBClient

# InfluxDB config
INFLUX_HOST = '<HOST>'
INFLUX_PORT = 8086
INFLUX_DB = '<DATABASE>'
client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT)
client.switch_database(INFLUX_DB)

# I2C bus setup
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize BME280
bme = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Initialize Lux Sensor (TSL2591)
lux_sensor = adafruit_tsl2591.TSL2591(i2c)
lux_sensor.gain = adafruit_tsl2591.GAIN_LOW
lux_sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS

# Initialize DS18B20 Probe
probe = W1ThermSensor()

print("Starting multi-sensor readout. Press Ctrl+C to stop.")

try:
    while True:
        timestamp = datetime.utcnow().isoformat()

        # Read BME280
        bme_t = float(bme.temperature)
        bme_h = float(bme.humidity)
        bme_p = float(bme.pressure)

        time.sleep(2)  # small pause between devices

        # Read DS18B20
        probe_t = float(probe.get_temperature())

        time.sleep(2)

        # Read Lux
        lux_val = float(lux_sensor.lux)

        # Print to terminal
        print(f"[{timestamp}] BME280: {bme_t:.2f}°C, {bme_h:.2f}%, {bme_p:.2f}hPa | "
              f"Probe: {probe_t:.2f}°C | Lux: {lux_val:.2f}")

        # Prepare Influx payload
        data = [
            {
                "measurement": "environment",
                "time": timestamp,
                "fields": {
                    "bme_temp": bme_t,
                    "bme_hum": bme_h,
                    "bme_press": bme_p,
                    "probe_temp": probe_t,
                    "lux": lux_val
                }
            }
        ]

        # Send to Influx
        client.write_points(data)

        # Wait until next 10-second cycle
        time.sleep(10)

except KeyboardInterrupt:
    print("\nLogging stopped.")
