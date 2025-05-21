from machine import Pin, ADC, I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

# LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
I2C_ADDR = i2c.scan()[0]

lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# MQ2 en GP27 (ADC1)
mq2 = ADC(27)

while True:
    valor = mq2.read_u16()
    lcd.putstr("Gas: {}\n".format(valor))
    lcd.clear
    if valor > 30000:
        lcd.putstr("¡ALERTA GAS!")
    else:
        lcd.putstr("Nivel seguro")
    time.sleep(1)
