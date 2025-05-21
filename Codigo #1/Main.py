# ================================================================
# Nombre del archivo: contador_boton.py
# Descripción: Incrementa un contador mostrado en pantalla OLED SSD1306
#              usando un botón conectado a la Raspberry Pi Pico W.
# Nombre: Ernesto Torres Pineda 22211665
# Fecha: 21/05/2025
# ================================================================
 
from machine import Pin, I2C
import ssd1306
import time

# Configurar I2C (ajusta los pines según tu conexión)
i2c = I2C(1, scl=Pin(27), sda=Pin(26))
print(i2c.scan())

# Inicializar la pantalla OLED (128x64)
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Configurar botón en GP15 (usa pull-up interno)
boton = Pin(15, Pin.IN, Pin.PULL_UP)

# Inicializar contador en cero
contador = 0
ultimo_estado = 1  # Estado anterior del botón

# Función para mostrar el contador
def mostrar_contador(valor):
    oled.fill(0)
    oled.text("Contador:", 0, 20)
    oled.text(str(valor), 60, 40)
    oled.show()

# Mostrar "0" al inicio
mostrar_contador(contador)

# Bucle principal
while True:
    estado = boton.value()
    if estado == 0 and ultimo_estado == 1:  # Flanco de bajada (botón presionado)
        contador += 1
        mostrar_contador(contador)
        time.sleep_ms(200)  # Anti-rebote
    ultimo_estado = estado
