from influxdb import InfluxDBClient
import board
import busio
import adafruit_tsl2591
from datetime import datetime

# I2C setup
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2591.TSL2591(i2c)

# Influx config
INFLUX_HOST = '<HOST>'  # Replace with your InfluxDB host
INFLUX_PORT = 8086
INFLUX_DB = '<DATABASE>'  # Replace with your InfluxDB database name

client = InfluxDBClient(host=INFLUX_HOST, port=INFLUX_PORT)
client.switch_database(INFLUX_DB)

# Set gain to low to prevent overflow
sensor.gain = adafruit_tsl2591.GAIN_LOW  # 1x gain

# Set integration time to 100ms
sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS

# Prepare the payload to send to InfluxDB
data = [{
    "measurement": "lux_data",
    "tags": {
        "sensor": "tsl2591",
        "location": "office"  # You can change this to your sensor's location
    },
    "time": datetime.utcnow().isoformat(),
    "fields": {
        "lux": float(sensor.lux)
    }
}]

# Ship the data to InfluxDB
client.write_points(data)

# Print the lux value
print(f"Lux: {sensor.lux:.2f} sent to InfluxDB")
