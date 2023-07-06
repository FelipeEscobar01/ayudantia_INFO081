import os

H_MAX = 24; H_MIN = 0; M_MAX = 59; M_MIN = 0
NOMBRES = ("Maria", "Fernando")
MENSAJES = ("ojala te mejores!!!!", "XD", "no he podido dormir en 2 semanas",
            "QUEEEEEEE", "te voy a bloquear", "que fome", "YAAAAAA",
            "como hay tao", "ojala te empeores...", "que pena la vd",
            "estos mensajes no tienen sentido", "si se",
            "la revolucion industrial y sus consecuencias han sido...",
            "me encanta esa bandaaa", "ya q vola", "shiuuu", "si cache",
            "KIEEE PERO COMOOOOOO", "media volaita", "voy a ser constituyente", 
            "dedicare mi vida al lol", "no se jugar ajedrez eso si")

# Estoy muy seguro que es una mala practica hacer esto, si a alguien le interesa:
# https://www.tutorialspoint.com/why-importing-star-is-a-bad-idea-in-python
# Lo mismo aplica para todos los lenguajes y en varios contextos. Otro ejemplo
# mas es "using namespace std" en C++. Lo hare igual porque debido a la barrera 
# de idioma se reduce la chance de que ocurra lo descrito en la referencia
from random import * 

# Estoy usando las constantes definidas globalmente, por eso no tengo ningun
# parametro
def genera_hora() -> str:
    hora = randint(H_MIN, H_MAX)
    if (hora < 10):
        hora = '0' + str(hora)
    else:
        hora = str(hora)
    minutos = randint(M_MIN, M_MAX)
    if (minutos < 10):
        minutos = '0' + str(minutos)
    else:
        minutos = str(minutos)
    return hora + ':' + minutos

def genera_hora_unica(horas_usadas: list[str]) -> str:
    hora = genera_hora()
    if (hora in horas_usadas):
        return genera_hora_unica(horas_usadas)
    horas_usadas.append(hora)
    return hora

def main():
    print(f"Esta bien manipular archivos aqui? {os.getcwd()}")
    seguir = int(input("Si? (1) No? (0): "))
    if (not seguir):
        return
    if ("mensajes.txt" in os.listdir()):
        print("Archivo ya existia, no se hara nada")
        return
    mensajes = list(MENSAJES)
    shuffle(mensajes)
    lineas = [] 
    horas_usadas = []
    for msg in mensajes:
        hora = genera_hora_unica(horas_usadas)
        nombre = NOMBRES[randint(0, 1)]
        lineas.append(f"{hora}/{nombre}/{msg}\n")
    with open("mensajes.txt", 'x') as archivo:
        for line in lineas:
            archivo.write(line)

if __name__ == "__main__":
    main()
