from machine import Timer, Pin
import time

timer = Timer(-1)

red = Pin(15, Pin.OUT)
blue = Pin(13, Pin.OUT)

def toggle_red(t):
    red.value(not red.value())

def toggle_blue(t):
    blue.value(not blue.value())

timer.init(mode=Timer.ONE_SHOT, period=5000, callback=toggle_red)
timer.deinit()
timer.init(mode=Timer.PERIODIC, period=100, callback=toggle_blue)
time.sleep_ms(500)
timer.deinit()
