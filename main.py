from machine import Pin
import time

botao = Pin(18, Pin.IN, Pin.PULL_UP)
led = Pin(23, Pin.OUT)

while True:
    estado = botao.value()

    if estado == 0:
        led.value(1)
        print("LED ativado")
    else:
        led.value(0)
        print("LED desativado")
        
    time.sleep(0.2)

#Wokwi simulator link: https://wokwi.com/projects/481616105278788609
