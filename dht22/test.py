#!/usr/bin/python3

import time
import DHT22_2
import pigpio

pi = pigpio.pi()
s = DHT22_2.sensor(pi, 4, LED=17, power=None)

s.trigger()
time.sleep(0.2)
print("{:5.1f} {:5.1f} {:5.1f} {} {} {} {}".format(
   s.humidity(), s.temperature(), s.staleness(),
   s.bad_checksum(), s.short_message(), s.missing_message(),
   s.sensor_resets()))


s.cancel()
pi.stop()

