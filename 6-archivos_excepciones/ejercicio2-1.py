import os


def main():
    archivos = os.listdir()
    if ("flujo_total_abril.txt" in archivos):
        print("Ya se ejecuto este programa, si quiere ejecutarlo denuevo"
              " borre el archivo \"flujo_total_abril.txt\".")
        return
    remedios = {}
    for i in range(1, 31):
        if (i < 10):
            nombre_archivo = f"0{i}-04-2023"    # Aca debiese haber tenido
        else:                                   # el .txt al final de la
            nombre_archivo = f"{i}-04-2023"     # string, perdon u.u
        try:
            with open(nombre_archivo, 'r') as archivo:
                for line in archivo:
                    texto = line.strip()
                    texto = texto.split('-')
                    try:
                        remedios[texto[0]] += int(texto[1])
                    except KeyError:
                        remedios[texto[0]] = int(texto[1])
        except FileNotFoundError:
            print(f"\"{nombre_archivo}\" no existe! terminando ejecucion")
            return 
    with open("flujo_total_abril.txt", 'w') as archivo:
        for x, drug in enumerate(remedios, 1):
            if (x != len(remedios)):
                archivo.write(f"{drug}-{remedios[drug]}\n")
            else:
                archivo.write(f"{drug}-{remedios[drug]}")


if __name__ == "__main__":
    main()
