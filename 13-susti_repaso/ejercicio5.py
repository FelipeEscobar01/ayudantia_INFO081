from random import *

L_MIN = 5; L_MAX = 20; N_MIN = 0; N_MAX = 50

def genera_ejercicio(size: int) -> tuple:
    lista = []
    l_size = 0
    while (l_size != size - 1):
        lista.append(randint(N_MIN, N_MAX))
        l_size += 1
    pos = randint(0, size - 1)
    lista.append(lista[pos])
    return (lista, lista[pos] * 2)

def two_sum(lista: list, suma: int) -> dict:
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if (lista[i] + lista[j] == suma):
                return {i: lista[i], j: lista[j], "suma": suma}

def main():
    ejercicio = genera_ejercicio(randint(L_MIN, L_MAX))
    print(ejercicio)
    print(two_sum(ejercicio[0], ejercicio[1]))

if __name__ == "__main__":
    main()