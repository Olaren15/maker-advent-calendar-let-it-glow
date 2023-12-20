# Imports
from machine import Pin
import time

# Set up input pins
red_button = Pin(2, Pin.IN, Pin.PULL_DOWN)
green_button = Pin(3, Pin.IN, Pin.PULL_DOWN)

# Set up output pins
red_led = Pin(14, Pin.OUT)

# Set up counter variable
count = 0

while True:

    time.sleep(0.2)

    red_led.value(0)  # LED off until button press

    if red_button.value() == 1:
        count = count - 1
        red_led.value(1)  # LED on
        print(count)

    if green_button.value() == 1:
        count = count + 1
        red_led.value(1)  # LED on
        print(count)
