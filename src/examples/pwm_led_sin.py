import machine
import time
import math

def pulse(l, t):
    for i in range(20):
         l.duty(int(math.sin(i / 10 * math.pi) * 500 + 500))
         time.sleep_ms(t)

BLUE_PIN = 13

blue_led = machine.Pin(BLUE_PIN)
pwm = machine.PWM(blue_led, freq=1000, duty=0)

for x in range(2):
    pulse(pwm, 100)
pwm.duty(0)
pwm.deinit()


