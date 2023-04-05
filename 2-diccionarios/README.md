
---
### _Los primeros tres ejercicios tendrán la solución post-ayudantia o en la misma si alcanza el tiempo, el último (sin contar "Topes de Horario") desafiense ustedes a hacer, aunque obvio cualquier duda preguntenme..._
---

## 🍉 **Ejercicio 1**

Escriba una función:

```
def elementos_que_comparten(lista1: list, lista2: list) -> tuple:
```

El nombre de la función, lo explica todo.

<br/>

# **Topes de Horario**

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
    estudiantes = {'Juan Perez': ['INFO081', 'INFO088', 'BAIN075'],
                   'Claudia Benavides': ['BAIN067', 'BAIN065', 'INFO088'],
                   'Xavi del Escoval': ['BAIN077', 'BAIN075', 'INFO081'],
                   'Bastian Gajardo': ['BAIN077', 'BAIN079', 'INFO088'],
                   'Jorge Maturana': ['INFO088', 'INFO081', 'BAIN077'],
                   'Josefina Vergara': ['BAIN079', 'BAIN065']}
```


## Con el objetivo de detectar topes de horario, se le solicita lo siguiente:

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