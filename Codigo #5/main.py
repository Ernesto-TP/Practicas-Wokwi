# ================================================================
# Lenguajes de Interfaz - TECNM Campus ITT
# Descripción: Indica cuando hay una inclinacion y los valores de esta, utilizando un accelerometro y giroscopio MPU6050.
# Nombre: Ernesto Torres Pineda 22211665       
# Fecha: 21/05/2025     
# ================================================================
from machine import Pin, I2C
from machine import Pin, I2C
import time
import ssd1306
from mpu6050 import MPU6050  # Asegúrate de tener el archivo mpu6050.py cargado

# Configuración del bus I2C 1 con pines GP27 (SCL) y GP26 (SDA)
i2c = I2C(1, scl=Pin(27), sda=Pin(26))

# Inicializa pantalla OLED 128x64
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# Inicializa el sensor MPU6050
mpu = MPU6050(i2c)

# Bucle principal
while True:
    datos = mpu.get_accel()
    ax = datos["x"]
    ay = datos["y"]
    
    oled.fill(0)
    oled.text("Alerta inclinación", 0, 0)
    oled.text("X: {}".format(ax), 0, 20)
    oled.text("Y: {}".format(ay), 0, 35)
    
    if abs(ax) > 15000 or abs(ay) > 15000:
        oled.text("¡Inclinado!", 0, 50)
    
    oled.show()
    time.sleep(0.5)
