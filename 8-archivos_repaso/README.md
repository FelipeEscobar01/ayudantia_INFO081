
## 🥑 **Ejercicio 1**

##### **Ejercicio extraido de Control 1 del ramo Taller Estructura de Datos y Algoritmos (2020)**

---
##### _Aunque cabe aclarar que yo redacte el enunciado porque era solo una parte de un ejercicio, la que valia menos puntos..._
---

<br/>

Escriba una funcion recursiva que me entregue la suma de los digitos impares que se encuentren en un numero.

Una regla eso si, no se puede trabajar con los numeros en formato string o lista ni nada del estilo, se tiene que trabajar con datos de tipo int.

**->** _El numero 943 tiene los digitos impares 9 y 3 por lo que la salida de la funcion recursiva debiese ser 9 + 3 = 12._

<br/>

## 🥑 **Ejercicio 2**

##### **Ejercicio extraido de Control 4 del ramo Programacion (Semestre pasado)**

<br/>

Escriba un programa en Python que dado dos numeros enteros **a** y **b**, muestre en pantalla el producto de dichos numeros usando el antiguo algoritmo de multiplicacion llamado **metodo de la multiplicacion rusa**. Este metodo no requiere conocer la tabla de multiplicar, aunque se necesita saber sumar, ademas de saber dividir entre 2.

Este metodo consiste en dividir (division entera) sucesivamente por 2 el numero **a** y duplicar el numero **b** hasta que **a** tome el valor de 1. Luego se suman todos los valores de **b** correspondientes a los valores de **a impares**. Asuma que los inputs son numeros enteros (no se solicita validar el registro). **Desarrolle usando recursividad**.

El siguiente ejemplo muestra la ejecucion de 23 por 48.

|a  |b  |¿Es a impar?  |A sumar   |
|---|---|--------------|----------|
|23|48|**si**|**48**|
|11|96|**si**|**96**|
|5|192|**si**|**192**|
|2|384|no||
|1|768|**si**|**768**|

**El resultado es 48 + 96 + 192 + 768 = 1104**

<br/>

## 🥑 **Ejercicio 3**

##### **Ejercicio extraido de Pre-Prueba 2 del ramo Programacion (Semestre pasado)**

<br/>

La Universidad Austral maneja el archivo **inscripciones_total.csv** con los registros de inscripcion de asignaturas de sus estudiantes en un archivo de texto en formato CSV que tiene los campos rut, nombre_estudiante, codigo_asignatura, nombre_asignatura, semestre, año, tal como se muestra en el siguiente ejemplo.

```
5-2,Maria Escobar,F-3,Taller 2,2,2022
4-2,Samantha Villaroel,F-5,Taller 3,1,2015
1-0,Javier Maturana,G-1,Geometria,2,2016
7-3,Maria Maturana,F-5,Taller 3,2,2017
6-3,Maria Vergara,F-5,Taller 3,1,2017
3-1,Ignacio Gajardo,F-2,Programacion,1,2023
5-2,Maria Escobar,G-1,Geometria,2,2022
...
```

Con el objeto de estructurar la informacion de mejor manera y reducir el espacio de almacenamiento devido a los miles de registros generados semestralmente, se solicita distribuir esta informacion en tres archivos distintos, que se hagan cargo de los estudiantes, las inscripciones y las asignaturas por separado (este proceso se llama "normalizacion" cuando se trabaja con bases de datos). El ejemplo de archivo anterior produciria los siguientes tres archivos:

**estudiantes.csv**
```
5-2,Maria Escobar
4-2,Samantha Villaroel
1-0,Javier Maturana
7-3,Maria Maturana
...
```

**inscripciones.csv**
```
F-3,Taller 2
F-5,Taller 3
G-1,Geometria
F-5,Taller 3
...
```

**asignaturas.csv**
```
5-2,F-3,2,2022
4-2,F-5,1,2015
1-0,G-1,2,2016
7-3,F-5,2,2017
...
```

Cree la funcion **normaliza(archivo_entrada: str) -> None:** que tome como entrada archivo_entrada y produzca los tres archivos (estudiantes.csv, inscripciones.csv y asignaturas.csv) correspondientes.

La funcion debe validar **mediante excepciones** que **archivo_entrada** exista y que ninguno de los tres archivos de salida exista.

---
##### _¿Y donde estan los archivos? Generenlos en base al archivo de python que deje en la carpeta "ejercicio3", porfavor intenten entender el codigo lo suficiente para ser capaces de recrearlo, intente comentarlo todo lo posible junto a los otros codigos como esta semana no puedo realizar la ayudantia, y si no quieren, estan los archivos que genere mientras resolvia yo los ejercicios._
---

<br/>