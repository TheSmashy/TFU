from influxdb import InfluxDBClient
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280
from datetime import datetime

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Influx config
INFLUX_HOST = '<HOST>'
INFLUX_PORT = 8086
INFLUX_DB = '<DATABASE>'

client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT)
client.switch_database(INFLUX_DB)

# Prepare payload
data = [{
    "measurement": "bme280",
    "tags": {
        "host": "pi-zero-test-rig",
        "location": "office"
    },
    "time": datetime.utcnow().isoformat(),
    "fields": {
        "temperature": float(bme280.temperature),
        "humidity": float(bme280.humidity),
        "pressure": float(bme280.pressure)
    }
}]

# Ship it
client.write_points(data)
