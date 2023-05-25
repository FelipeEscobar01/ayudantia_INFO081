# Ejercicio extraido de Control 1 del ramo Taller Estructuras de Datos y Algoritmos (2020)

def reduce_recursivo(num: int) -> int:
    """
    Recibe un numero, retorna la suma de los digitos impares que se
    encuentren en el numero.
    """

    # Eventualmente el numero que reciba la funcion sera 0, por la
    # division entera que se entrega cuando llamo a la funcion.

    if (num > 0):

        # "num % 2 == 1" me entregara si el ultimo digito de mi numero
        # es impar con un valor booleano proveniente de la igualdad.

        if (num % 2 == 1):

        #
        #                          943
        #                           |
        #                       943 % 2 = 1
        #                           |
        #                      943 % 10 = 3     // Lo sumo con...
        #                           |
        #                     943 // 10 = 94    // Lo que salga de este
        #                                       // llamado.
        #

            return num % 10 + reduce_recursivo(num // 10)

        else:

        #
        #                           94
        #                           |
        #                        94 % 2 = 0
        #                           |
        #                           0           // Lo sumo con...
        #                           |
        #                      94 // 10 = 94    // Lo que salga de este
        #                                       // llamado.
        #

            return 0 + reduce_recursivo(num // 10)
    
    # Cuando num sea cero, retorno 0 y la suma acumulada en la pila
    # se efectuara.

    return 0


def main():
    print("\nIngrese 0 para terminar la ejecucion!\n")
    x = int(input("x: "))
    while (x != 0):
        print(f"Suma digitos impares de {x} = {reduce_recursivo(x)}")
        x = int(input("x: "))


if __name__ == "__main__":
    main()

