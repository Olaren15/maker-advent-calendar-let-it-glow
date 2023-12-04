from machine import Pin
import time

red = Pin(14, Pin.OUT)

for i in range(10):
    red.value(1)
    time.sleep(0.5)

    red.value(0)
    time.sleep(0.5)
