import os

# Le entrego alias a 'random' para poder invocar sus funciones/modulos
# como r.randint() y asi.
import random as r

# Modifica la variable 'PRINT' por un valor distinto de 0 si se quiere
# ver como funciona el codigo en el momento de ejecucion.
PRINT = 1

NOMBRES = ("Felipe", "Claudia", "Fabian", "Nicolas", "Ursula", "Alexis",
           "Antonia", "Javier", "Josefina", "Enrique", "Martin", "Jorge",
           "Samantha", "Jose", "Ignacio", "Rodrigo", "Maria", "Eliana",
           "Osvaldo")
APELLIDOS = ("Espinoza", "Vergara", "Escobar", "Castro", "Araya", 
             "Gajardo", "Sanchez", "Messi", "Sanchez", "Maturana",
             "Ferrada", "Villaroel", "Ruiz", "Flores", "Barrientos", 
             "Ramirez", "De la Maza")
RAMOS = (("C-1", "Calculo 1"), ("C-2", "Calculo 2"), 
         ("F-2", "Programacion"), ("F-1", "Intro"),
         ("F-3", "Taller 2"), ("F-4", "Datos"),
         ("F-5", "Taller 3"), ("G-1", "Geometria"),
         ("A-1", "Algebra"), ("A-2", "Algebra Lineal"))


def main():
    print(f"Directorio actual: {os.getcwd()}")
    ejecutar = input("Si es el directorio correcto ingrese \'1\': ")
    if (ejecutar == '1'):

        # Chequeo si el archivo ya existe.
        archivos = os.listdir()
        if ("inscripciones_totales.csv" in archivos):
            print("El archivo ya existe en este directorio, eliminelo " \
                  "para situaciones no deseadas...")
            # Si existe retorno desde la funcion main (Termino el
            # programa).
            return

        cant_estudiantes = int(input("Cantidad de estudiantes a generar: "))
        estudiantes = {}

        # Hice esta lista solo por comodidad y ahorrarme manejo de
        # excepciones.
        rut_ya_ingresados = []

        for i in range(cant_estudiantes):

            nombre_apellido = (NOMBRES[r.randint(0, len(NOMBRES) - 1)] 
                              + ' '                                    
                              + APELLIDOS[r.randint(0, len(APELLIDOS) - 1)])
            if (nombre_apellido in list(estudiantes.keys())) :
                nombre_apellido = (NOMBRES[r.randint(0, len(NOMBRES) - 1)] 
                                  + ' '                                    
                                  + APELLIDOS[r.randint(0, len(APELLIDOS) - 1)])

            rut_estudiante = r.randint(1, cant_estudiantes + 1)
            if (rut_estudiante in rut_ya_ingresados):
                rut_estudiante = r.randint(1, cant_estudiantes + 1)
            rut_ya_ingresados.append(rut_estudiante)
            
            ramos_estudiante = []
            for i in range(r.randint(1, 3)):
                ramos_estudiante.append(RAMOS[r.randint(0, len(RAMOS) - 1)])
           
            # Hasta aqui tengo del estudiante:
            # - Nombre.
            # - RUT.
            # - Ramos de el.
            # x Semestre del ramo.
            # x Año del ramo.
            # Las ultimas dos las voy a hacer en la misma asignacion en 
            # el diccionario ya que es algo mas sencillo.
            estudiantes[nombre_apellido] = (
            #              - RUT -                          - RAMOS - 
            f"{rut_estudiante}-{rut_estudiante // 2}", tuple(ramos_estudiante),
            #   - SEMESTRE -              - AÑO -
            str(r.randint(1, 2)), str(r.randint(2015, 2023))
            )

            # Para conveniencia dejare todos sus ramos inscritos en el
            # mismo semestre y año.

        if (PRINT):
            print("------------" * 6)
            print("Estudiantes:")
            for llave in estudiantes:
                print(f"{llave}: {estudiantes[llave]}")
            print("------------" * 6)

        # Ahora voy a hacer algo ineficiente pero que necesito hacer con
        # tal de añadirle mas desafio al ejercicio o que se haga de la forma
        # en que se espere se haga.
            
        strings_a_escribir = []
        for estudiante in estudiantes:
            for ramo in estudiantes[estudiante][1]:
               strings_a_escribir.append(f"{estudiantes[estudiante][0]},{estudiante},{ramo[0]},{ramo[1]},{estudiantes[estudiante][2]},{estudiantes[estudiante][3]}\n")

        # Queria poder hacer esto jejeje.
        r.shuffle(strings_a_escribir)

        if (PRINT):
            print("------------" * 6)
            print("Strings a escribir en el archivo:")
            for cadena in strings_a_escribir:
                print(cadena, end='')
            print("------------" * 6)

        # Y ahora a escribir en el archivo.
        with open("inscripciones_totales.csv", 'w') as archivo:
            for cadena in strings_a_escribir:
                archivo.write(cadena)

if __name__ == "__main__":
    main()

