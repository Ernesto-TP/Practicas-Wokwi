# ================================================================
# Lenguajes de Interfaz - TECNM Campus ITT
# Descripción: Muestra los valores medidos de un sensor DHT22
# Nombre: Ernesto Torres Pineda 22211665       
# Fecha: 21/05/2025     
# ================================================================
from machine import Pin, I2C
from machine import I2C, Pin   
from time import sleep

from pico_i2c_lcd import I2cLcd
from dht import DHT22

i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# direccion I2C
I2C_ADDR = i2c.scan()[0]

# crear objeto tipo lcd
dht = DHT22(Pin(5))
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# loop
while True:
    dht.measure()
    temp = dht.temperature()
    hum = dht.humidity()
    print("Temperature: {}°C   Humidity: {:.1f}% ".format(temp, hum))
    
    lcd.clear()
    lcd.putstr('Temp: ' + str(temp) + " C")
    lcd.move_to(0,1)
    lcd.putstr('Hum: ' + str(hum) + "%")
    sleep(2)
