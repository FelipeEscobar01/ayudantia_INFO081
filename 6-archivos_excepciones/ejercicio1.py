import os


def main():
    matriz = []

    with open("ejercicio1.txt", 'r') as ejercicio1:
        for line in ejercicio1:             # Recorro cada linea del archivo.
            matriz.append(line)             # Apendo a matriz cada una.

    for i in range(len(matriz)):            # Recorro cada fila de matriz.
        matriz[i] = matriz[i].strip()           # Elimino '\n'.
        matriz[i] = matriz[i].split('-')        # Separo en sub-strings.

    for fila in matriz:                     # fila = ['1', '2', '3', ...]
        for i in range(len(fila)):              # Recorro fila de inicio a fin.
            fila[i] = int(fila[i])                  # '1' = 1, '2' = 2, '3' = 3, ...

    # Listo, ahora tenemos una matriz de enteros en base a la informacion
    # que estaba en el archivo!

    # La matriz esta dispuesta en [0..n] para las divisiones
    # y de [1..n] para los dias del ultimo mes.

    print("¿Cual es la division que mas ha vendido durante el ultimo mes?")

    division = 0
    mayor_venta = 0

    for i in range(len(matriz[0])):             # Recorriendo largo columnas
        venta = 0
        for j in range(len(matriz)):            # Recorriendo largo filas
            venta += matriz[j][i]
        if (venta >= mayor_venta):
            mayor_venta = venta
            division = i
    print(f"La division que mas vendio fue la division {division}, \n"
          f"vendio {mayor_venta} productos.")

    print("¿Cual es la division que menos ha vendido durante el ultimo mes?")

    menor_venta = venta
    for i in range(len(matriz[0])):         
        venta = 0
        for j in range(len(matriz)):
            venta += matriz[j][i]
        if (venta <= menor_venta):
            menor_venta = venta
            division = i
    print(f"La division que menos vendio fue la division {division}, \n"
          f"vendio {menor_venta} productos.")

    print("¿Que dia vendieron mas las divisiones en conjunto?")

    dia = 0
    mayor_venta = 0
    for i in range(len(matriz)):                # Recorriendo largo filas
        venta = 0
        for j in range(len(matriz[0])):         # Recorriendo largo columnas
            venta += matriz[i][j]
        if (venta >= mayor_venta):
            mayor_venta = venta
            dia = i
    dia += 1
    print(f"El dia que mas se vendio fue el {dia} del ultimo mes, \n"
          f"se vendio {mayor_venta} productos.")


if __name__ == "__main__":
    main()
