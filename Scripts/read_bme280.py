import board
import busio
from adafruit_bme280 import basic as adafruit_bme280

# Set up I²C
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize BME280
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c, address=0x76)

# Print readings
print(f"Temperature: {bme280.temperature:.1f} °C")
print(f"Humidity:    {bme280.humidity:.1f} %")
print(f"Pressure:    {bme280.pressure:.1f} hPa")
