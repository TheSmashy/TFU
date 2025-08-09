import time
import board
import busio
import adafruit_tsl2591

# Setup I2C and Lux Sensor
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_tsl2591.TSL2591(i2c)

# Set gain to low to prevent overflow
sensor.gain = adafruit_tsl2591.GAIN_LOW  # 1x gain

# Set integration time to 100ms
sensor.integration_time = adafruit_tsl2591.INTEGRATIONTIME_100MS

# Print heading
print("Lux Sensor Reading:")
print("Press Ctrl+C to exit.")

# Start reading data
try:
    while True:
        lux = sensor.lux
        print(f"Lux: {lux:.2f}")  # Print lux value with two decimal places
        time.sleep(1)  # Update every second

except KeyboardInterrupt:
    print("\nLogging stopped.")
