# Ejercicio extraido de Control 4 del ramo Programacion (Semestre pasado)

# Una aclaracion, este codigo no funciona, bien...
# Intenten poner 4 en el multiplicando y 3 en el multiplicador, no da
# el valor deseado, pero esta era la forma que se me ocurrio hacer el
# codigo y el profe tenia la misma solucion en la pauta jajaja.

def multiplicacion_rusa(num1: int, num2: int) -> int:
    if (num2 == 1):
        return num1
    else:
        # Si "num2" es impar, dejo como a sumar su valor.
        if (num2 % 2 == 1):
            return num2 + multiplicacion_rusa(num1 * 2, num2 // 2)
        # Si es par, continuo con la ejecucion.
        else:
            return multiplicacion_rusa(num1 * 2, num2 // 2)


def main():
    print("\nIngrese 0 para terminar la ejecucion!\n")
    x = int(input("Multiplicando: "))
    y = int(input("Multiplicador: "))
    while (x != 0 and y != 0):
        print(f"{x} * {y} = {multiplicacion_rusa(x, y)}")
        x = int(input("x: "))
        y = int(input("y: "))

if __name__ == "__main__":
    main()

