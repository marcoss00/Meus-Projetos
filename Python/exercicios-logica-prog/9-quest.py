import time

segundos = 0
minutos = 0
horas = 0

while 0 < 1:
    segundos = segundos + 1
    time.sleep(0.5)
    print("segundos: " + str(segundos))
    print("minutos: " + str(minutos))
    print("horas: " + str(horas))
    if segundos == 60:
        segundos = 0
        minutos = minutos + 1
    if minutos == 60:
        segundos = 0
        minutos = 0
        horas = horas + 1
