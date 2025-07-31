from machine import Pin
from utime import sleep

print("Hello World!")

Led_Vermelho = Pin(15, Pin.OUT)
Led_Amarelo = Pin(16, Pin.OUT)
Led_Verde = Pin(17, Pin.OUT)

while True:
    Led_Verde.on()
    print("LED VERDE LIGADO!")
    sleep(20)
    Led_Verde.off()
    print("LED VERDE DESLIGADO!")

    sleep(0.5)

    Led_Amarelo.on()
    print("LED AMARELO LIGADO!")
    sleep(10)
    Led_Amarelo.off()
    print("LED AMARELO DESLIGADO!")

    sleep(0.5)

    Led_Vermelho.on()
    print("LED VERMELHO LIGADO!")
    sleep(7)
    Led_Vermelho.off()
    print("LED VERMELHO DESLIGADO!")

    sleep(0.5)