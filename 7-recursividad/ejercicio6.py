
import random


LARGO_LISTA = 20
RANDOM_MINIMO = 1
RANDOM_MAXIMO = 30


def busqueda_binaria(lista: list[int], valor_a_buscar: int) -> int:
    """ 
    Recibe una lista con datos de tipo entero y un dato del mismo tipo
    a buscar dentro de esta, retorna el indice en donde se encuentra el
    dato.
    """
    if (lista == []):
        return -1
    mediana = len(lista) // 2
    if (valor_a_buscar < lista[mediana]):
        return busqueda_binaria(lista[:mediana - 1], valor_a_buscar)
    elif (valor_a_buscar == lista[mediana]):
        return mediana
    return busqueda_binaria(lista[mediana + 1:], valor_a_buscar)


def busqueda_binaria_v2(lista: list[int], inicio: int, fin: int,
                        valor_a_buscar: int) -> int:
    """
    Recibe una lista con datos de tipo entero, el inicio y fin de esta,
    y el valor a buscar dentro de la lista, retorna el indice en donde
    se encuentra el dato.
    """
    if (inicio > fin):
        return -1
    mediana = (inicio + fin) // 2
    if (valor_a_buscar < lista[mediana]):
        return busqueda_binaria_v2(lista, inicio, mediana - 1, valor_a_buscar)
    elif (valor_a_buscar == lista[mediana]):
        return mediana
    return busqueda_binaria_v2(lista, mediana + 1, fin, valor_a_buscar)


def main():
    lista = []
    for i in range(LARGO_LISTA):
        lista.append(random.randint(RANDOM_MINIMO, RANDOM_MAXIMO))
    lista.sort()
    valor_a_buscar = -1
    while (valor_a_buscar < RANDOM_MINIMO 
           or valor_a_buscar > RANDOM_MAXIMO):
        valor_a_buscar = int(input("Ingrese valor a buscar\n> "))
    print(lista)
    print(busqueda_binaria(lista, valor_a_buscar))
    print(busqueda_binaria_v2(lista, 0, len(lista) - 1, valor_a_buscar))


if __name__ == "__main__":
    main()

