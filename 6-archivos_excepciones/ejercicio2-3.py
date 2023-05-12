import os


def main():
    menor_venta = 0
    try:
        with open(f"01-04-2023", 'r') as archivo:
            for x, line in enumerate(archivo):
                if (x == 8):    # Posicion Venlafaxina
                    texto = line.strip()
                    texto = texto.split('-')
                    menor_venta = int(texto[1])
    except FileNotFoundError:
        print(f"\"{nombre_archivo}\" no existe! terminando ejecucion")
        return
    dia = 0
    for i in range(2, 31):
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
                        if (int(texto[1]) <= menor_venta):
                            menor_venta = int(texto[1])
                            dia = i
        except FileNotFoundError:
            print(f"\"{nombre_archivo}\" no existe! terminando ejecucion")
            return 
    print(f"Dia de la menor venta es el dia {dia}, " \
          f"la menor venta como tal es {menor_venta} unidades")


if __name__ == "__main__":
    main()
