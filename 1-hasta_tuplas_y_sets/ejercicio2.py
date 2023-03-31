import random


def n_de_datos_mayores_al_promedio(lista: list) -> int:
    """
    Recibe lista, retorna el numero de datos mayores al promedio en la
    lista.
    """
    contador = 0
    promedio = sum(lista) / len(lista)
    for elemento in lista:
        if elemento > promedio:
            contador += 1
    return contador


def lista_random(rango1: int, rango2: int, largo: int) -> list:
    """
    Recibe rango1 (Se asume es el inicio del rango), rango2 (fin del
    rango), ambos para el randint usado dentro de la funcion y ademas
    el largo de la lista deseada
    """
    lista = []
    for i in range(0, largo):
        lista.append(random.randint(rango1, rango2 + 1))
    return lista


def main():
    lista = lista_random(0, 50, 10)
    print(lista)
    print("Promedio: ", sum(lista) / len(lista))
    print(n_de_datos_mayores_al_promedio(lista))


if __name__ == "__main__":
    main()
