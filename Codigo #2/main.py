# ================================================================
# Lenguajes de Interfaz - TECNM Campus ITT
# Descripción: Muestra los valores de un sensor LDR en pantalla 
# Nombre: Ernesto Torres Pineda 22211665       
# Fecha: 21/05/2025     
# ================================================================

from machine import ADC, Pin, I2C
import ssd1306
import time

# Configura la pantalla OLED con I2C en GP0 (SDA) y GP1 (SCL)
i2c = I2C(1, scl=Pin(27), sda=Pin(26))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# LDR en GP26 (ADC0)
ldr = ADC(Pin(28))  # Asegúrate de tener el divisor de voltaje correctamente conectado

while True:
    valor = ldr.read_u16()  # Lectura de 0 a 65535
    voltaje = 3.3 * valor / 65535  # Convertir a voltaje si se desea
    oled.fill(0)
    oled.text("Medidor de luz", 0, 0)
    oled.text("Valor ADC:", 0, 20)
    oled.text(str(valor), 0, 35)
    oled.show()
    time.sleep(1)
