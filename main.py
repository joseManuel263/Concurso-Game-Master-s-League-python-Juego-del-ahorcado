import time
import random

nombreJugador = input(f"¿como te llamas?\n(̶◉͛‿◉̶) \n\n")
print(f"hola {nombreJugador}\n\n¿estas listo para jugar?\n\n")

time.sleep(2)

print(f"listo o no {nombreJugador}\n")
time.sleep(2.5)

print("comienza en 3\n")
time.sleep(1)
print("2\n")
time.sleep(1)
print("1\n")
time.sleep(1)
print("0\n")
time.sleep(1)

print("Comienza a adivinar\nbuena suerte\n(^◡^ )\n")

time.sleep(1.5)

numeroPalabra = random.randint(1,9)

palabra0 = "auto"
palabra1 = "casa"
palabra2 = "concurso"
palabra3 = "proyectos"
palabra4 = "plataforma"
palabra5 = "recuerda"
palabra6 = "python"
palabra7 = "electrónico"
palabra8 = "esfuerzo"

palabra = ""

if numeroPalabra == 1:
    palabra = palabra0
elif numeroPalabra == 2:
    palabra = palabra1
elif numeroPalabra == 3:
    palabra = palabra2
elif numeroPalabra == 4:
    palabra = palabra3
elif numeroPalabra == 5:
    palabra = palabra4
elif numeroPalabra == 6:
    palabra = palabra5
elif numeroPalabra == 7:
    palabra = palabra6
elif numeroPalabra == 8:
    palabra = palabra7
elif numeroPalabra == 9:
    palabra = palabra8


respuestaJugador = ""

vidas = 5

while vidas > 0:
    fallas = 0
    for letra in palabra:
        if letra in respuestaJugador:
            print(letra, end="")
        else:
            print("_", end="")
            fallas = fallas + 1
    if fallas == 0:
        input()
        print(f"\nFelicidades {nombreJugador}\n\nganaste\n(>‿◠)\n")
        input()
        break

    letraJugador = input(f"\nIntroduca tu letra {nombreJugador}\n")
    respuestaJugador += letraJugador

    if letraJugador not in palabra:
        vidas = vidas - 1
        print(f"lo siento {nombreJugador}\npero te equivocaste\n¯\_( ͡❛ ͜ʖ ͡❛)_/¯")
        time.sleep(2)
        print(f"te quedan {vidas} vidas")
    if vidas == 0:
        print(f"{nombreJugador} acabas de perder\n(╥︣﹏᷅╥)")
else:
    input()
    print(f"Gracias por participar {nombreJugador}\nmejor suerte para la proxima")
    input()
