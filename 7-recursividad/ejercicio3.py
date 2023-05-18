
def invertir_palabra(palabra: list[str], inicio: int, fin: int) -> None:
    """
    Recibe una string con cada caracter separado en una lista, un entero
    indicando el indice de inicio y otro el de fin, no retorna nada.
    """
    if (inicio >= fin):
        return
    palabra[inicio], palabra[fin] = palabra[fin], palabra[inicio]
    return invertir_palabra(palabra, inicio + 1, fin -1)


def main():
    palabra = list(input("Ingrese palabra\n> "))
    invertir_palabra(palabra, 0, len(palabra) - 1) 
    palabra = ''.join(palabra)
    print(palabra)


if __name__ == "__main__":
    main()

