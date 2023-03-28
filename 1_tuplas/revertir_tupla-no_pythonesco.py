def revertir_tupla(tupla: tuple) -> tuple:
    """
    Recibe una tupla, retorna una nueva tupla con los datos originales
    dispuestos al reves.
    """
    lista_temp = []
    for i in range(0, len(tupla)):
        # En realidad esta forma de trabajar tan "no pythonesco" no es,
        # pero algo si.
        lista_temp.append(tupla[(len(tupla) - 1) - i])
    return tuple(lista_temp)


def main():
    tupla1 = (1, 2, 3, 4, 5)
    print(revertir_tupla(tupla1), '\n')

    tupla2 = (1, 2, 3, 4)
    print(revertir_tupla(tupla2))


if __name__ == "__main__":
    main()
