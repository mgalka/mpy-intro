import machine
import time

BLUE_PIN = 13

blue_led = machine.Pin(BLUE_PIN)
pwm = machine.PWM(blue_led, freq=1000, duty=0)

for x in range(0, 1024, 10):
    pwm.duty(x)
    time.sleep(.01)

for x in range(1023, -1, -10):
    pwm.duty(x)
    time.sleep(.01)
pwm.deinit()


