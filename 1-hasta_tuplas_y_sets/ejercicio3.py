def maximo_comun_divisor(num1: int, num2: int) -> int:
    """
    Recibe 2 datos de tipo entero, retorna el maximo comun divisor 
    entre estos
    """
    maximo_comun_divisor = 0
    for i in range(1, min(num1, num2) + 1):
        if (num1 % i == 0) and (num2 % i == 0):
            maximo_comun_divisor = i
    return maximo_comun_divisor


def main():
    num1 = int(input("Numero 1\n> "))
    num2 = int(input("Numero 2\n> "))
    print(maximo_comun_divisor(num1, num2))


if __name__ == "__main__":
    main()
