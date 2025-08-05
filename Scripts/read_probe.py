 #!/usr/bin/python
from w1thermsensor import W1ThermSensor
import time
sensor = W1ThermSensor()
start = time.time()
temp_c = sensor.get_temperature()
elapsed = time.time() - start
#print(f"DS18B20 Temp: {temp_c:.2f} °C")
print(f"Read time: {elapsed:.2f}s Temp: {temp_c:.2f}")
