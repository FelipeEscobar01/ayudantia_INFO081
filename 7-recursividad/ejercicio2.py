
def es_primo(posible_primo: int, divisor: int) -> bool:
    if (divisor == 1):
        return True
    if (posible_primo % divisor == 0):
        return False
    return (True and es_primo(posible_primo, divisor - 1))


def main():
    posible_primo = int(input("Posible primo\n> "))
    if (es_primo(posible_primo, posible_primo - 1)):
        print(f"{posible_primo} es primo!")
    else:
        print(f"{posible_primo} no es primo!")


if __name__ == "__main__":
    main()

