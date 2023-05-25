# Ejercicio extraido de Pre-Prueba 2 del ramo Programacion (Semestre pasado)

# Modifica la variable 'PRINT' por un valor distinto de 0 si se quiere
# ver como funciona el codigo en el momento de ejecucion.
PRINT = 1

def normaliza(archivo_entrada: str) -> None:
    """
    Recibe un archivo de entrada, separa su informacion en tres nuevos
    archivos, no retorna nada.
    """
    try:

        # Abro archivo a leer y extraigo de el todas las lineas.
        with open(archivo_entrada, 'r') as archivo:
            informacion_archivo = archivo.readlines()            

        estudiantes = []
        asignaturas = []
        inscripciones = []

        for linea in informacion_archivo:
    
            # Realizo un split cada caracter coma sobre la linea con
            # el caracter de salto de linea eliminado.
            informacion = linea.strip().split(',')

            if (PRINT):
                print("------------" * 6)
                print("Linea luego del split en las comas:")
                print(informacion)
                print("------------" * 6)

            # Chequeo que no haya guardado ya el estudiante, si se quiere
            # ver a que corresponde cada posicion recuerda poner 
            # 'PRINT' en 1.
            if ((informacion[0], informacion[1]) not in estudiantes):
                estudiantes.append((informacion[0], informacion[1]))
            asignaturas.append((informacion[2], informacion[3]))
            inscripciones.append((informacion[0], informacion[2],
                                  informacion[4], informacion[5]))

            if (PRINT):
                print("------------" * 6)
                print("A escribir en:")
                print(f"estudiantes.csv: {informacion[0]},{informacion[1]}")
                print(f"asignaturas.csv: {informacion[2]},{informacion[3]}")
                print(f"inscripciones.csv: {informacion[0]},{informacion[2]},"
                      f"{informacion[4]},{informacion[5]}")
                print(informacion)
                print("------------" * 6)

        # ¿Que hace el argumento 'x' al abrir el archivo?
        # Abro el archivo EXCLUSIVAMENTE para su creacion y modificacion
        # se genera una excepcion en el momento que este archivo ya exista
        # de ahi el "except FileExistsError".
        with open("estudiantes.csv", 'x') as primer_archivo:
            for linea in estudiantes:
                # Uso una f-string por que aveces es impredecible (al
                # menos para mi el como maneja python los saltos de linea
                # y tambien a veces el como lo imprime cuando se pasa
                # como otro argumento.
                primer_archivo.write(f"{linea[0]},{linea[1]}\n")
        with open("asignaturas.csv", 'x') as segundo_archivo:
            for linea in asignaturas:
                segundo_archivo.write(f"{linea[0]},{linea[1]}\n")
        with open("inscripciones.csv", 'x') as tercer_archivo:
            for linea in inscripciones:
                tercer_archivo.write(f"{linea[0]},{linea[1]},{linea[2]},{linea[3]}\n")

    except FileNotFoundError:
        print(f"ERROR: el archivo {archivo_entrada} no existe")
    except FileExistsError:
        print(f"ERROR: uno de los archivos de destino ya existe")
    finally:
        return


def main():
    normaliza("inscripciones_totales.csv")


if __name__ == "__main__":
    main()
