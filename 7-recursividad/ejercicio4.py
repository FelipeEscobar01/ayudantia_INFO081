
def es_palindromo(posible_palindromo: list[str], inicio: int,
                  fin: int) -> bool:
    if (inicio >= fin):
        return True
    elif (posible_palindromo[inicio] != posible_palindromo[fin]):
        return False
    return (True and es_palindromo(posible_palindromo, inicio + 1, fin - 1))


def main():
    posible_palindromo = list(input("Ingrese posible palindromo\n> "))
    print(es_palindromo(posible_palindromo, 0, len(posible_palindromo) - 1))


if __name__ == "__main__":
    main()
