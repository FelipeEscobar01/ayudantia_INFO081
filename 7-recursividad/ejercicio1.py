
def factorial(num: int) -> int:
    if (num == 0):
        return 1
    return num * factorial(num - 1)


def main():
    num = int(input("Factorial a obtener\n> "))
    print(f"El factorial de {num} es {factorial(num)}")
     

if __name__ == "__main__":
    main()

