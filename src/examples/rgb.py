import machine
import utime as time

RED_PIN, GREEN_PIN, BLUE_PIN = 15, 12, 13


def turn_off(*args):
    for pin in args:
        pin.off()

def demo():
    red = machine.Pin(RED_PIN, machine.Pin.OUT)
    green = machine.Pin(GREEN_PIN, machine.Pin.OUT)
    blue = machine.Pin(BLUE_PIN, machine.Pin.OUT)
    turn_off(red, green, blue)
    for pin in (red, green, blue):
        pin.on()
        time.sleep(1)
        pin.off()
        time.sleep(0)


if __name__ == '__main__':
    demo()
 
