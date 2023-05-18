
PRINTEAR_DICCIONARIO = True 


def fibonacci(fib: int) -> int:
    """
    Recibe un entero correspondiente a que numero de la secuencia de
    fibonacci se desea, lo retorna.
    """
    if (fib <= 1):
        return 0 
    elif (fib == 2):
        return 1 
    return fibonacci(fib - 1) + fibonacci(fib - 2)


def fibonacci_con_memoizacion(fib: int, diccionario = {}) -> int:
    """
    Recibe un entero correspondiente a que numero de la secuencia de
    fibonacci se desea, ademas un diccionario donde almacenar aquellos
    ya procesados, retorna el numero de fibonacci.
    """
    if (fib <= 1):
        return 0
    elif (fib == 2):
        return 1
    if (fib not in diccionario):
        diccionario[fib] = fibonacci_con_memoizacion(fib - 1, diccionario) \
                           + fibonacci_con_memoizacion(fib - 2, diccionario)
        if (PRINTEAR_DICCIONARIO):
            for llave in diccionario:
                print(f"{llave} -> {diccionario[llave]}")
            print()
    return diccionario[fib]


def main():
    fib = int(input("Fibonacci que se desea\n> "))
    con_memoizacion = input("¿Con memoizacion?\n(0) -> No"
                            "\t(1) -> Si\n> ")
    if (con_memoizacion == '0'):
        print(fibonacci(fib))
    else:
        print(fibonacci_con_memoizacion(fib))


if __name__ == "__main__":
    main()
