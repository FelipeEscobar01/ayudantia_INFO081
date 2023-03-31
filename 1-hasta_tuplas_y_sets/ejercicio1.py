def son_pitagoricos(cateto1: int, cateto2: int, 
                    hipotenusa: int) -> bool:
    """
    Recibe dos catetos y una hipotenusa, retorna si es o no un trio
    pitagorico
    """
    return ((cateto1 ** 2) + (cateto2 ** 2) == (hipotenusa ** 2))


def main():
    lista_input = []
    for i in range(0, 3):
        lista_input.append(int(input("> ")))
    print(son_pitagoricos(lista_input[0], lista_input[1], lista_input[2]))


if __name__ == "__main__":
    main()
