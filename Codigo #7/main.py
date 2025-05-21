from machine import Pin, ADC, I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

# LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, i2c.scan()[0], 2, 16)

# Potenciómetro en GP26 (ADC0)
pot = ADC(26)

while True:
    valor = pot.read_u16()
    voltaje = (valor / 65535) * 3.3
    lcd.clear()
    lcd.putstr("Pot: {}\n".format(valor))
    lcd.putstr("Volt: {:.2f} V".format(voltaje))
    time.sleep(0.5)
