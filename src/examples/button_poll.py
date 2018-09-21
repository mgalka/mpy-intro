import machine
import utime as time

RED_PIN, GREEN_PIN, BLUE_PIN = 15, 12, 13
BUTTON_PIN = 4

red_pin = machine.Pin(RED_PIN, machine.Pin.OUT)
green_pin = machine.Pin(GREEN_PIN, machine.Pin.OUT)
blue_pin = machine.Pin(BLUE_PIN, machine.Pin.OUT)

led_pins = (red_pin, green_pin, blue_pin)

button = machine.Pin(BUTTON_PIN, machine.Pin.IN)

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

if __name__ == '__main__':
    pins_off(led_pins)
    led_pin = cycle(led_pins)
    pin = None
    while True:
        if not button.value():
            print('Button pressed')
            if pin:
                pin.off()
            pin = next(led_pin)
            pin.on()
        time.sleep(.2)
    
