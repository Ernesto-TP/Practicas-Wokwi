# ================================================================
# Lenguajes de Interfaz - TECNM Campus ITT
# Descripción: Muestra el incremento o decremento de opciones dependiendo 
#               de uno de los dos botones presionados
# Nombre: Ernesto Torres Pineda 22211665       
# Fecha: 21/05/2025     
# ================================================================
from machine import Pin, I2C
import ssd1306
import time

# Configuración OLED
i2c = I2C(1, scl=Pin(27), sda=Pin(26))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Botones
btn_up = Pin(14, Pin.IN, Pin.PULL_UP)
btn_down = Pin(15, Pin.IN, Pin.PULL_UP)

opciones = ["Opción 1", "Opción 2", "Opción 3"]
indice = 0

while True:
    if not btn_up.value():
        indice = (indice + 1) % len(opciones)
        time.sleep(0.2)
    elif not btn_down.value():
        indice = (indice - 1) % len(opciones)
        time.sleep(0.2)
    
    oled.fill(0)
    oled.text("Selector:", 0, 0)
    oled.text(opciones[indice], 0, 30)
    oled.show()
    time.sleep(0.1)
