import machine

adc = machine.ADC(0)

while True:
    print(adc.read())
