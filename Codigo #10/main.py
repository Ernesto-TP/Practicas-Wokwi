# ================================================================
# Nombre del archivo: contador_boton.py
# Descripción: Muestra los valores seleccionados de un keypad de 16 botones
# Nombre: Ernesto Torres Pineda 22211665
# Fecha: 21/05/2025
# ================================================================
from machine import Pin, I2C
from lcd_api import LcdApi
from i2c_lcd import I2cLcd
import time

# LCD
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)
lcd = I2cLcd(i2c, i2c.scan()[0], 2, 16)

# Keypad 4x4
keys = [
    ["1", "2", "3", "A"],
    ["4", "5", "6", "B"],
    ["7", "8", "9", "C"],
    ["*", "0", "#", "D"]
]

rows = [Pin(i, Pin.OUT) for i in range(4, 8)]
cols = [Pin(i, Pin.IN, Pin.PULL_DOWN) for i in range(8, 12)]

def scan_keypad():
    for i, row in enumerate(rows):
        row.high()
        for j, col in enumerate(cols):
            if col.value():
                row.low()
                return keys[i][j]
        row.low()
    return None

while True:
    key = scan_keypad()
    if key:
        lcd.clear()
        lcd.putstr("Tecla:\n{}".format(key))
        time.sleep(0.3)  # evitar múltiples lecturas
