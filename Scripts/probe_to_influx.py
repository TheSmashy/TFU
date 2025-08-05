from influxdb import InfluxDBClient
import board
import busio
from adafruit_bme280 import basic as adafruit_bme280
from w1thermsensor import W1ThermSensor
from datetime import datetime

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# DS18B20 setup
ds18b20 = W1ThermSensor()

# InfluxDB config
INFLUX_HOST = '<HOST>'
INFLUX_PORT = 8086
INFLUX_DB = '<DATABASE>'

client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT)
client.switch_database(INFLUX_DB)

# Read sensors
#bme_temp = float(bme280.temperature)
#humidity = float(bme280.humidity)
#pressure = float(bme280.pressure)
#time.sleep(1.5)  # wait before polling the probe
probe_temp = float(ds18b20.get_temperature())  # °C

# Prepare payload
now = datetime.utcnow().isoformat()
data = [
    {
        "measurement": "ds18b20",
        "tags": {
            "host": "pi-zero-test-rig",
            "sensor": "contact-probe",
            "location": "office"
        },
        "time": now,
        "fields": {
            "temperature": probe_temp
        }
    }
]

# Send to Influx
client.write_points(data)
