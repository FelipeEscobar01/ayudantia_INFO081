
---
### _Los primeros tres ejercicios tendrán la solución post-ayudantia o en la misma si alcanza el tiempo, el último desafiense ustedes a hacer, aunque obvio cualquier duda preguntenme..._
---

 Una cortita aclaración antes, deje de poner en **negrita** y _cursiva_ ciertos apartados de cada ejercicio porque siento que derrota un objetivo de aprendizaje que es el saber extraer la información correcta de un enunciado y hacer lo que se pide y no otra cosa. 

<br/>

## 🍉 **Ejercicio 1**

Escriba una función:

```
def elementos_que_comparten(lista1: list, lista2: list) -> tuple:
```

El nombre de la función se explica a ella misma.

(Definir las listas con un largo 10 y poner valores aleatorios entre 1 y 50)

<br/>

## 🍉 **Ejercicio 2**

Tengo el siguiente diccionario:

```
    signos = {'Aries':       ((3, 21), (4, 20)),
              'Tauro':       ((4, 21), (5, 21)),
              'Geminis':     ((5, 22), (6, 21)),
              'Cancer':      ((6, 22), (7, 23)),
              'Leo':         ((7, 24), (8, 23)),
              'Virgo':       ((8, 24), (9, 23)),
              'Libra':       ((9, 24), (10, 23)),
              'Escorpio':    ((10, 24), (11, 22)),
              'Sagitario':   ((11, 23), (12, 21)),
              'Capricornio': ((12, 22), (1, 20)),
              'Acuario':     ((1, 21), (2, 19)),
              'Piscis':      ((2, 20), (3, 20))}
```

Escriba la función:

```
def determinar_signo_zodiacal(signos: dict, fecha_de_nacimiento: tuple) -> str:
```

Cabe aclarar que la tupla "fecha_de_nacimiento" tiene el siguiente formato:

```
(year|month|day)
```

¡Además pido al usuario que me entregue las tres casillas de información de la tupla!

La salida de la función es unicamente el signo al que pertenece la información almacenada en la tupla.

<br/>

## 🍉 **Ejercicio 3**

### **Topes de Horario**

La Facultad de Ciencias de la Ingeniería se encuentra implementando un sistema para optimizar la creación de horarios para asignaturas que se dictan en el Campus Miraflores. La implementación mantiene por una parte un diccionario con los horarios de cada asignatura, el cual tiene el siguiente aspecto:

```
    asignaturas = {'INFO081': ['LU2', 'JU1'],
                   'BAIN075': ['MA1', 'JU1'],
                   'BAIN079': ['MA1', 'JU1'],
                   'BAIN077': ['LU1', 'MI2'],
                   'INFO088': ['VI1', 'MI3'],
                   'BAIN067': ['VI2', 'MI1'],
                   'BAIN065': ['VI1', 'MI4']}
```

Por otra parte, se mantiene un diccionario con las asignaturas inscritas por cada estudiante, el cual tiene la siguiente forma:

```
    estudiantes = {'Juan Perez': ['INFO081', 'INFO088', 'BAIN075', 'BAIN065'],
                   'Claudia Benavides': ['BAIN067', 'BAIN065', 'INFO088'],
                   'Xavi del Escoval': ['BAIN077', 'BAIN075', 'INFO081'],
                   'Bastian Gajardo': ['BAIN077', 'BAIN079', 'INFO088'],
                   'Jorge Maturana': ['INFO088', 'INFO081', 'BAIN077'],
                   'Josefina Vergara': ['BAIN079', 'BAIN065', 'BAIN075']}
```

### **Con el objetivo de detectar topes de horario, se le solicita lo siguiente:**

Cree la función:

```
def horarios_de_tope(asignaturas: dict, asig1: string, asig2: string) -> tuple:
```

Recibe el diccionario de asignaturas y el nombre de dos de ellas, y retorna una tupla con los horarios en común entre ambas.

Cree la función:

```
def detecta_conflictos(estudiante: str, ramos_inscritos: list, asignaturas: dict) -> tuple:
```

Que recibe el nombre de un estudiante, una lista con los nombres de las asignaturas que inscribió, y el diccionario con los horarios de todas las asignaturas, y retorna una tupla con los horarios en los cuales ese estudiante tiene tiene tope de horario.

Salida esperada:

```
Conflictos de Juan Perez:
('JU1', 'VI1')
Conflictos de Claudia Benavides:
('VI1',)
Conflictos de Xavi del Escoval:
('JU1',)
Conflictos de Bastian Gajardo:
()
Conflictos de Jorge Maturana:
()
Conflictos de Josefina Vergara:
('MA1', 'JU1')
```

<br/>

## 🍉 **Ejercicio 4**

Tengo el siguiente diccionario:

```
    alternativas_estudiantes = {'Pregunta 1': ('A', 'A', 'C', 'A', 'B'),
                                'Pregunta 2': ('D', 'E', 'D', 'A', 'B'),
                                'Pregunta 3': ('A', 'A', 'A', 'A', 'B'),
                                'Pregunta 4': ('C', 'B', 'A', 'X', 'D'),
                                'Pregunta 5': ('E', 'C', 'B', 'A', 'D'),
                                'Pregunta 6': ('E', 'E', 'E', 'E', 'E'),
                                'Pregunta 7': ('A', 'A', 'B', 'C', 'E'),
                                'Pregunta 8': ('E', 'X', 'A', 'D', 'A'),
                                'Pregunta 9': ('D', 'D', 'D', 'D', 'D'),
                                'Pregunta 10': ('A', 'A', 'B', 'C', 'X')}
```

Cree la función:

```
def alternativas_marcadas(alternativas_estudiantes: dict) -> dict:
```

Esta función debe retornar las alternativas marcadas de forma independiente, si se marco 2 veces la alternativa A, debiese retornar solo una A y asi consecutivamente, recordar que las X son estudiantes que no marcaron ninguna alternativa, por lo que no tienen que ser incluidas en la salida de nuestro programa.

Salida esperada:

```
Pregunta 1 :  ('A', 'B', 'C')
Pregunta 2 :  ('A', 'B', 'D', 'E')
Pregunta 3 :  ('A', 'B')
Pregunta 4 :  ('A', 'B', 'C', 'D')
Pregunta 5 :  ('A', 'B', 'C', 'D', 'E')
Pregunta 6 :  ('E',)
Pregunta 7 :  ('A', 'B', 'C', 'E')
Pregunta 8 :  ('A', 'D', 'E')
Pregunta 9 :  ('D',)
Pregunta 10 :  ('A', 'B', 'C')
```

### **Como se puede ver las alternativas estan ordenadas...**