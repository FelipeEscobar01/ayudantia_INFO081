import random


def llenado_aleatorio_de_lista(LARGO: int, RANGO_MIN: int, 
                               RANGO_MAX: int) -> list:
    """
    Recibe LARGO, RANGO_MIN y RANGO_MAX, retorna una lista de largo
    LARGO con elementos aleatorios que van desde RANGO_MIN hasta 
    RANGO_MAX.
    """
    lista = []
    for i in range(LARGO):
        lista.append(random.randint(RANGO_MIN, RANGO_MAX))
    return lista


def elementos_que_comparten(lista1: list, lista2: list) -> tuple:
    """
    Recibe dos listas, retorna una tupla con exclusivamente aquellos
    elementos que comparten ambas.
    """
    return tuple(set(lista1) & set(lista2))


def main():
    LARGO = 10
    RANGO_MIN = 1
    RANGO_MAX = 50
    lista1 = llenado_aleatorio_de_lista(LARGO, RANGO_MIN, RANGO_MAX)
    lista2 = llenado_aleatorio_de_lista(LARGO, RANGO_MIN, RANGO_MAX)
    print(lista1, '\n', lista2)
    print(elementos_que_comparten(lista1, lista2))


if __name__ == "__main__":
    main()
