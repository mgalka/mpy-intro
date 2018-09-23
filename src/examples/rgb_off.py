import machine

RED_PIN, GREEN_PIN, BLUE_PIN = 15, 12, 13
red = machine.Pin(RED_PIN, machine.Pin.OUT)
green = machine.Pin(GREEN_PIN, machine.Pin.OUT)
blue = machine.Pin(BLUE_PIN, machine.Pin.OUT)

for pin in (red, green, blue):
    pin.off()

print('RGB off!')