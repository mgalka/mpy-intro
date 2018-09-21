---
title: MicroPython, czyli szybki start w IoT
author: Michał Gałka
footer: Michał Gałka
---

# MicroPython

## MicroPython

- Implementacja języka Python 3.
- Zawiera niewielki podzbiór funkcji bibilioteki standardowej.
- Zoptymalizowana do działania w środowiska o ograniczonych zasobach, takich jak mikrokontrolery.

## MicroPython

- Zawiera zaawansowane mechanizmy takie jak:
    - Interaktywna linia poleceń.
    - Dowolna precyzja liczb całkowitych.
    - Domknięcia, list comprehensions, generatory.
    - Obsługa wyjątków
- Ma niewielkie zużycie pamięci:
    - 256 kB ROM (code).
    - 16 kB RAM.

## MicroPython

- MicroPython dostępny jest dla wielu konfiguracji sprzętowych:
    - `pyboard`
        - Referencyjna płytka deweloperska.
- Oficjalne porty:
    - `WiPy`
        - plafoma sprzętowa oparta od ESP32 stworzona przez PyCom.
    - `ESP8266` 
        - Niskobudżetowy mikroprocesor stworzony przez firmę Espressif Systems.
        - Używany w wielu modułach i zestawach deweloperskich.
    - `ESP32`
        - Następca mikroprocesora ESP8266
    - `unix`
        - Wersja interpretera MicroPython działająca na systemach uniksowych.

# Zestaw deweloperski

## ESP8266

- Procesor wyprodukowany przez Espressif Systems.
- @ 80 MHz
- 32 KiB pamięci RAM na instrukcje.
- 80 KiB pamięci RAM na dane.
- do 16 MiB pamięci flash podłączonej po SPI.
    - Z reguły 512 KiB do 4 MiB.
- We/Wy
    - 16 pinów GPIO
    - SPI (programowo lub sprzętowo)
    - I2C (możliwe programowo)
    - UART + dodatkowy UART tylko do wysyłania danych.
    - 10 bitowy przetwornik AD
- WiFi
    - 802.11 b/g/n.
    - Szyfrowanie WEP, WPA/WPA2.
    - Pracuje jako urządzenie lub Access Point.


## ESP12F

- Moduł oparty o ESP8266.
- Zawiera antenę do WiFi.
- Pamięć Flash 4MB.

## Witty Mini

- Płytka deweloperska oparta o moduł ESP12F.
    - Dodatkowe peryferia:
        - Dioda RGB.
        - Czujnik światła.
        - Przycisk.
        - Regulator napięcia + port mcro USB do zasilania.
- Płytka pomocnicza:
    - Konwerter TTL -> USB (konsola szerwgowa)
    - Przyciski `flash` i `reset` 

## Witty Mini

![](img/common/WittyMini_overview.png)

## Witty Mini

![](img/common/WittyMini_buttons.png)

## Witty Mini

![](img/common/WittyMini_ports.png)

# Podłączenie zestawu deweloperskiego

## Terminal szeregowy

- Po podłączeniu kabla microUSB do płytki pomocniczej w systemie operacyjnym widoczny jest nowy port szeregowy.
- należy się do niego podłączyć przy pomocy terminala szeregowego (PuTTY)

## Terminal - Windows

![](img/flashing-instructions/03-windows_serial_port.png)

## Terminal - Windows

::: columns

:::: column
![](img/installation-instructions/windows/02-putty_config_serial_params.png)
::::

:::: column
![](img/installation-instructions/windows/03-putty_config_save.png)
::::

:::

## Terminal - Linux/Unix/Mac

- Połączenie przy pomocy terminala `picocom`

```
picocom -b 115200 /dev/tty.wchusbserial14150
```

- Opcja `-b` ustawia prędkość połączenia
- `/dev/tty.wchusbserial14150` - ścieżka do portu szeregowego.

## REPL
- Po podłączeniu do terminala pojawia się znak zachęty interpretera Python.
- REPL (Read Eval Print Loop)
    - Pracuje w trybie interaktywnym.
    - Przetwarza komendy języka.
    - Wykonuje je po naciścięciu klawisza `Enter`.
    - Wyświetla wyniki.

## ampy
- Otwarte narzędzie stworzone przez firmę `Adafruit`.
- Wykorzystuje REPL i połączenie szeregowe do obsługi typowych czynności związanych z rozwojem oprogramowania.
- Automatyzuje operacje takie jak:
    - Ładowanie plików na urządzenie.
    - Pobieranie plików z urządzenia.
    - Uruchamianie lokalnych skryptów na urządzeniu.
    - Wyświetlanie listy plików na urządzeniu.
    - Tworzenie i usuwanie katalogów na urządzeniu.

## Konfiguracja WiFi

- Konfiguracja urządzenia jako klienta sieci WiFi

```python
import network

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect('SSID', 'secret_key')
```

- Istnieje także możliwość skonfigurowania ESP8266 w trybie AccessPoint.

## Konfiguracja WiFi

- Wyświetlenie konfiguracji sieciowej.

```python
import network

station = network.WLAN(network.STA_IF)
print(station.ifconfig())
```

## WebREPL
- Pozwala na dostęp do REPL przez WiFi.
- Daje możliwość pobierania i ładowania plików na urządzenie.
- Wymagania:
    - Urządzenie skonfigurowane i podłączone do sieci WiFi.
    - WebREPL włączony na urządzeniu.
    - Pobrany zestaw narzędzi WebREPL.

## Uruchomienie WebREPL

- Połączenie z REPL przez port szeregowy.
- Uruchomienie następujących komend:

```python
>>> import webrepl_setup
WebREPL daemon auto-start status: disabled

Would you like to (E)nable or (D)isable it running on boot?
(Empty line to quit)
> E
To enable WebREPL, you must set password for it
New password (4-9 chars): secret
Confirm password: secret
Changes will be activated after reboot
Would you like to reboot now? (y/n) y
>>>
```

# GPIO

## GPIO

- GPIO - general-purpose input/output. 
- Pin interfejsu do komunikacji między elementami systemu komputerowego.
- Może pracować jako wejście lub wyjście.
    - Często jest to właściwość konfigurowalna.

## GPIO
- Piny GPIO bywają grupowane w porty.
- Często są wyprowadzane w formie wtyczek lub gniazd na płytkach deweloperskich.
- Każdy pin cyfrowy może znajdować się w stanie **wysokim (1)** lub **niskim (0)**.

## GPIO OUTPUT
- Dla pinów wyjściowych mamy możliwość ustawienia ich stanu z poziomu programu.
- MicroPython posiada odpowiednie funkcje w module `machine`.
    - Każdy pin posiada swój numer.
    - Operacje na pinach zaimplementowane są w klasie `machine.Pin`
    - Konstruktor wymaga podania numeru pina i trybu jego pracy.


## GPIO OUTPUT
```python
RED_PIN = 15
red = machine.Pin(RED_PIN, machine.Pin.OUT)
red.on()
red.off()

red.value(1)
red.value(0)
```

## machine.Signal

- W niektórych przypadkach sygnały na pinach mogą dawać odwrotne efekty.
    - Stan niski włącza urządzenie.
    - Stan wysoki wyłącza urządzenie.
- klasa `machine.Signal` dodaje warstwę abstrakcji dla stanu pinów.
    - Daje możliwość odzwierciedlenia stanu urządzenia, a nie pinu.

## machine.Signal

```python
from machine import Pin, Signal

RED_RGB_PIN = 15 # active-high
BLUE_PIN = 2 # active-low

red_pin = Pin(RED_RGB_PIN, Pin.OUT)
blue_pin = Pin(BLUE_PIN, Pin.OUT)
red = Signal(red_pin, invert=False)
blue = Signal(blue_pin, invert=True)

red.value(1)
blue.value(1)

red.on()
blue.on()
```

## GPIO INPUT
- W trybie wejściowym stan pinu jest ustawiany przez urządzenie zewnętrzne.
- Z poziomu programu odczytujemy stan pinu.





