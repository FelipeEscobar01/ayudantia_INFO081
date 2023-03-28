def revertir_tupla(tupla: tuple) -> tuple:
    """
    Recibe una tupla, retorna una nueva tupla con los datos originales
    dispuestos al reves.
    """
    return tupla[::-1] 


def main():
    tupla1 = (1, 2, 3, 4, 5)
    print(revertir_tupla(tupla1), '\n')

    tupla2 = (1, 2, 3, 4)
    print(revertir_tupla(tupla2))
    

if __name__ == "__main__":
    main()
