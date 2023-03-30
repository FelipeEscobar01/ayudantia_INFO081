import random

def crea_tupla_random(rango: tuple, largo: int) -> tuple:
    """
    Recibe un rango en forma de tupla propuesto como "rango(inicio, 
    fin), un entero indicando el largo que se quiere para la tupla a
    retornar y finalmente se retorna la tupla creada.
    """
    lista_temp = []
    for i in range(0, largo):
        lista_temp.append(random.randint(rango[0], rango[1] + 1))
    return tuple(lista_temp)


def encontrar_moda(datos: tuple) -> int:
    """
    Recibe datos almacenados en una tupla, retorna la moda de estos
    datos a lo largo de la tupla.
    """
    datos_sin_repetir = list(set(datos))    # Tupla -> Set -> Lista
    mayores_repeticiones = datos.count(datos_sin_repetir[0]) 
    moda = datos_sin_repetir[0]
    for i in range(1, len(datos_sin_repetir)):
        dato_actual_se_repite = 0
        for j in range(0, len(datos)):
            if datos[j] == datos_sin_repetir[i]:
                dato_actual_se_repite += 1
        if (dato_actual_se_repite > mayores_repeticiones):
            moda = datos_sin_repetir[i]
    return moda


def main():
    tupla_random = crea_tupla_random((1, 10), 20)
    moda = encontrar_moda(tupla_random)
    print(tupla_random, '\n', moda)


if __name__ == "__main__":
    main()
