from machine import Pin, Signal

RED_RGB_PIN = 15
BLUE_PIN = 2


red_pin = Pin(RED_RGB_PIN, Pin.OUT)
blue_pin = Pin(BLUE_PIN, Pin.OUT)

red_pin.value(1)
blue_pin.value(0)

red = Signal(red_pin, invert=False)
blue = Signal(blue_pin, invert=True)

red.value(1)
blue.value(1)

red.on()
blue.on()