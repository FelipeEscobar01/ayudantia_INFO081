## 🍉 **Ejercicio 1**

Quiero almacenar los numeros de fibonacci en cierto rango (0, n] dentro de un diccionario, asi puedo luego preguntarle al usuario que valor de los procesados quisiese saber.

Disposición propuesta para el codigo:

```
def almacena_fibonacci(num: int) -> dict:
    ---
def consulta_baul(baul: dict) -> None:
    ---
def main():
    ---
if __name__ == "__main__":
    main()
```

##### _¿Qué es la sucesión de fibonacci? Es una serie numerica que empieza con los valores 0 y 1, siguiendo tras ellos la suma de los numeros anteriores, en este caso 0 + 1 = 1, luego tengo que evaluar la suma 1 + 1 = 2, luego 1 + 2 = 3 y asi..._

<br/>

## 🍉 **Ejercicio 2**

##### **Fuente: Prueba Nº1 2022**

<br/>

La Escuela de Ingeniería Civil en Informática tiene un sistema en donde mantiene los datos de sus estudiantes, los cursos que componen la carrera y las matrículas de estudiantes en cursos en dos diccionarios y una lista, respectivamente.

En el caso de los estudiantes, la clave es el RUT, y el valor es una tupla que contiene su nombre y correo:

```
    estudiantes = { "1-1" : ("Juan", "juan@gmail.com"), 
                    "2-2" : ("Claudia", "clau@uach.cl"),
                    …
                  }
```

En el caso de los cursos, la clave es la sigla, y el valor una tupla con el nombre, los créditos, el ciclo al que pertenecen (básico, licenciatura o profesional) y una lista con las siglas de los cursos requisitos.

```
    cursos = { "c-1" : ("Cálculo 1", 6, "Básico", []),
               "c-2" : ("Cálculo 2", 6, "Básico", ["c-1"]),
               "bd-1" : ("Bases de Datos", 5, "Licenciatura", ["p-2","c-1"]),
               "ps-1" : ("Proyectos de Software", 6, "Profesional", ["c-2", "so-1"]),
                …
             }
```

Las matrículas se almacenan en una lista de tuplas. Cada tupla contiene el RUT del estudiante, la sigla de la asignatura, el año y semestre en que se cursó, y la nota y el estado de la matrícula (aprobado, reprobado o pendiente).

```
    matriculas = [("1-1", "c-1", 2020, 1, 2.4, "Reprobado"), 
                  ("1.1", "p-1", 2020, 1, 5.4, "Aprobado"),
                  ("2-2", "c-1", 2020, 1, 4.2, "Aprobado"),
                   …]
```

**a)** Implemente la función:

```
def aviso_reprobados(matriculas: list, estudiantes: dict, cursos: dict, ciclo: str, anno: int, sem: int) -> tuple:
```

Que retorna una tupla con los correos (sin repetir) de los estudiantes que el año y semestre indicados, reprobaron asignaturas del ciclo indicado.

**b)** Implemente la función:

```
def avance_ciclo(matriculas: list, estudiantes: dict, cursos: dict, RUT: str) -> dict:
```

Que retorne un diccionario que contenga la cantidad de cursos de cada ciclo que ha sido aprobado por un alumno en particular, en donde la clave es el nombre del ciclo, y el valor un entero con el número de ciclos.

Datos y plantilla a usar:

```

estudiantes = {"1-1" : ("Juan", "juan@gmail.com"), 
               "2-2" : ("Claudia", "clau@uach.cl"),
               "3-3" : ("María", "mary@bla.com"),
               "4-4" : ("Andrés", "afer@hotmail.com")
              }
cursos = {"c-1" : ("Cálculo 1", 6, "Básico", []),
          "c-2" : ("Cálculo 2", 6, "Básico", ["c1"]),
          "p-1" : ("Progra 1", 6, "Básico", []),
          "p-2" : ("Progra 2", 6, "Básico", ["p-1","c-1"]),
          "bd-1" : ("Bases de Datos", 5, "Licenciatura", ["p-2","c-1"]),
          "so-1" : ("Sistemas Operativos", 5, "Licenciatura", ["p-2","bd-1"]),
          "ps-1" : ("Proyectos de software", 6, "Profesional", ["c-2", "so-1"])
         }
matriculas = [("1-1", "c-1", 2017, 1, 2.4, "Reprobado"),
              ("1-1", "c-1", 2017, 2, 5.2, "Aprobado"), 
              ("1-1", "p-1", 2017, 1, 5.4, "Aprobado"),
              ("1-1", "p-2", 2017, 2, 6.3, "Aprobado"),
              ("1-1", "c-2", 2018, 1, 4.0, "Aprobado"),
              ("1-1", "bd-1", 2018, 1, 5.2, "Aprobado"),
              ("1-1", "so-1", 2018, 2, 3.8, "Reprobado"),
              ("2-2", "c-1", 2017, 1, 4.2, "Aprobado"),
              ("2-2", "p-1", 2017, 1, 5.6, "Aprobado"),
              ("2-2", "c-2", 2017, 2, 3.5, "Reprobado"),
              ("2-2", "p-2", 2017, 2, 4.7, "Aprobado"),
              ("2-2", "c-2", 2018, 1, 3.3, "Aprobado"),
              ("2-2", "bd-1", 2018, 1, 5.1, "Aprobado"),
              ("2-2", "so-1", 2018, 2, 4.0, "Aprobado"),
              ("2-2", "ps-1", 2018, 2, 3.2, "Reprobado"),
              ("2-2", "ps-1", 2019, 1, 6.0, "Aprobado")]


def aviso_reprobados(matriculas: list, estudiantes: dict, cursos: dict,
                     ciclo: str, anno: int, sem: int) -> tuple:
    pass


def avance_ciclo(matriculas: list, estudiantes: dict, cursos: dict, 
                 RUT: str) -> dict:
    pass


def main():
    print(aviso_reprobados(matriculas, estudiantes, cursos, "Básico", 2017, 1))
    print(aviso_reprobados(matriculas, estudiantes, cursos, "Profesional", 2018, 2))
    print(avance_ciclo(matriculas, estudiantes, cursos, "1-1"))
    print(avance_ciclo(matriculas, estudiantes, cursos, "2-2"))


if __name__ == "__main__":
    main()
```                                                           

La salida esperada es:

```
('juan@gmail.com',)
('clau@uach.cl',)
{'Básico': 4, 'Licenciatura': 1, 'Profesional': 0}
{'Básico': 4, 'Licenciatura': 2, 'Profesional': 1}                                                          
```                                                            
                                                              
<br/>
                                                              
## 🍉 **Ejercicio 3**
                                                            
##### **Fuente: Segunda Evaluación 2022**
                                                              
<br/>
                                                              
El Departamento de Turismo de la Municipalidad de Valdivia está interesado en la entretención de sus veraneantes, para ello, solicita colaboración a un grupo de estudiantes de Ingeniería Civil en Informática para gestionar dicha información. Escriba un programa en Python que almacene la información de los turistas en un diccionario cuya llave es un código interno del turista, y el valor es una tupla que contiene: nombre, código entretenimiento, cantidad de días a la semana que asiste.

```
turistas = {132 : ("Mario Vasquez", 6, 3),
            13 : ("Maria Ines Campos", 11, 4),
            58 : ("Vicente Cush", 5, 4),
            342 : ("Mario Neta", 7, 2),
            789 : ("Eliza Noriega", 7, 5),
            76 : ("Amalia Alvarez", 2, 3),
            87 : ("Adolfo Rivera", 7, 1)
            }
```

Por ejemplo, el turista 789, su nombre es Eliza Noriega, participa en la entretención 7, y asiste 5 veces a la semana. Considere que el diccionario puede tener muchas personas, no solo los del ejemplo.
                                                              
Por otro lado, existe una lista de tuplas con las entretenciones disponibles y una puntuación (de 1 a 7) entregada por los usuarios de acuerdo a su grado de conformidad con ella. El índice de la lista representa el código entretenimiento. Por ejemplo, la primera entretención (código 0) es Buceo y la puntuación es 5.

```
entretencion = [("Buceo", 5), ("Masajes", 6), ("Casino", 4), 
                ("Piscina", 7), ("Playa", 4), ("Surf", 7),
                ("Baile entretenido", 2), ("Teatro", 5), ("Restaurant", 6),
                ("Karaoke", 4), ("Bingo", 7), ("Cine", 5), 
                ("Bar", 1), ("Spa", 5), ("Gimnasio", 4), 
                ("Cabalgata", 2)]
```

Implemente las siguientes funciones:

```
def filtrar(entretencion: list, puntuacion: int) -> list:
```

Que recibe como parámetro la  lista entretención y un entero. La función debe retornar una lista con las entretenciones cuya puntuación sea mayor o igual a la nota pasada por parámetro.

```
def promedio_dias(turistas: dict, entretencion: list, e: str) -> float:
```

Que recibe como parámetro el diccionario turistas, la lista entretención y un string con el nombre de una entretención en particular. La función debe retornar el promedio de días que acuden las personas a dicha entretención.

```
def usuarios_por_entretencion(turistas: dict, entretencion: list) -> dict:
```

Que recibe como parámetro el diccionario turistas y la lista entretención. Esta función debe retornar un diccionario que asocie el nombre de la entretención a una lista de códigos de turistas que asiste a ella. La lista debe estar ordenada en forma ascendente. Si la entretención no tiene usuarios, no la incluya en el diccionario.

Datos y plantilla a usar:

```
turistas = {132 : ("Mario Vasquez", 6, 3),
            13 : ("Maria Ines Campos", 11, 4),
            58 : ("Vicente Cush", 5, 4),
            342 : ("Mario Neta", 7, 2),
            789 : ("Eliza Noriega", 7, 5),
            76 : ("Amalia Alvarez", 2, 3),
            87 : ("Adolfo Rivera", 7, 1)
            }
entretencion = [("Buceo", 5), ("Masajes", 6), ("Casino", 4), 
                ("Piscina", 7), ("Playa", 4), ("Surf", 7),
                ("Baile entretenido", 2), ("Teatro", 5), ("Restaurant", 6),
                ("Karaoke", 4), ("Bingo", 7), ("Cine", 5), 
                ("Bar", 1), ("Spa", 5), ("Gimnasio", 4), 
                ("Cabalgata", 2)]


def filtrar(entretencion: list, puntuacion: int) -> list:
    pass


def promedio_dias(turistas: dict, entretencion: list, 
                  e: str) -> float:
    pass


def usuarios_por_entretencion(turistas: dict, 
                              entretencion: list) -> dict:
    pass


def main():
    print(filtrar(entretencion, 6))
    print("Promedio:", promedio_dias(turistas, entretencion, "Teatro"))
    print("Promedio:", promedio_dias(turistas, entretencion, "Bar"))
    entretencion_personas = usuarios_por_entretencion(turistas, entretencion)
    print(entretencion_personas)



if __name__ == "__main__":
    main()
```

La salida esperada es:

```
['Masajes', 'Piscina', 'Surf', 'Restaurant', 'Bingo']
Promedio: 2.6666666666666665
Promedio: -1
{'Baile entretenido': [132], 'Cine': [13], 'Surf': [58], 'Teatro': [87, 342, 789], 'Casino': [76]}
```