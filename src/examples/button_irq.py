from machine import Pin
import utime as time

RED_PIN, GREEN_PIN, BLUE_PIN = 15, 12, 13
BUTTON_PIN = 4

red_pin = Pin(RED_PIN, Pin.OUT)
green_pin = Pin(GREEN_PIN, Pin.OUT)
blue_pin = Pin(BLUE_PIN, Pin.OUT)

led_pins = (red_pin, green_pin, blue_pin)

button = Pin(BUTTON_PIN, Pin.IN)

def pins_off(pins):
    for pin in pins:
        pin.off()

def cycle(seq):
    idx = 0
    while True:
        yield seq[idx]
        if idx < (len(seq)-1):
            idx += 1
        else:
            idx = 0

def toggle_led(pin):
    pins_off(led_pins)
    next(led_pin).on()

if __name__ == '__main__':
    pins_off(led_pins)
    led_pin = cycle(led_pins)
    button.irq(trigger=Pin.IRQ_FALLING, handler=toggle_led)
    while True:
        time.sleep(.1)

