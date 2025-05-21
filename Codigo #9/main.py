# ================================================================
# Lenguajes de Interfaz - TECNM Campus ITT
# Descripción: Muestra la distancia detectada por un sensor ultrasonico HC-SR04
# Nombre: Ernesto Torres Pineda 22211665
# Fecha: 21/05/2025
# ================================================================
from machine import Pin, I2C, time_pulse_us
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

# LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, i2c.scan()[0], 2, 16)

# HC-SR04
trig = Pin(2, Pin.OUT)
echo = Pin(3, Pin.IN)

def medir_distancia():
    trig.low()
    time.sleep_us(2)
    trig.high()
    time.sleep_us(10)
    trig.low()
    duracion = time_pulse_us(echo, 1, 30000)  # timeout en µs
    distancia = duracion * 0.0343 / 2
    return distancia

while True:
    d = medir_distancia()
    lcd.clear()
    lcd.putstr("Distancia:\n{:.1f} cm".format(d))
    time.sleep(0.5)
