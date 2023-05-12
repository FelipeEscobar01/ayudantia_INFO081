import os


def main():
    mayor_venta = 0
    dia = 0
    for i in range(1, 31):
        if (i < 10):
            nombre_archivo = f"0{i}-04-2023"
        else:
            nombre_archivo = f"{i}-04-2023"
        try:
            with open(nombre_archivo, 'r') as archivo:
                for x, line in enumerate(archivo):
                    if (x == 8):    # Posicion Venlafaxina
                        texto = line.strip()
                        texto = texto.split('-')
                        if (int(texto[1]) >= mayor_venta):
                            mayor_venta = int(texto[1])
                            dia = i
        except FileNotFoundError:
            print(f"\"{nombre_archivo}\" no existe! terminando ejecucion")
            return 
    print(f"Dia de la mayor venta es el dia {dia}, " \
          f"la mayor venta como tal es {mayor_venta} unidades")


if __name__ == "__main__":
    main()
