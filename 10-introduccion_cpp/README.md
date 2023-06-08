## 🍓 **Ejercicio 1**

Hacer un programa que pregunte por el radio de una circunferencia y luego imprima el perimetro y el area de esta.

Hay que hacer uso de la libreria "cmath" para poder elevar, basta con escribir en la cabecera del programa lo siguiente:

```
#include <iostream> // Ya estaba de antes.
#include <cmath>
...
```

**PD:** _Da igual que valor se use para 𝝅, yo usé 3.141_

<br/>

## 🍓 **Ejercicio 2**

Lo mismo, solo que haciendo uso de un _**#define**_ en la cabecera del programa o un data type con el "prefijo" _**const**_.

<br/>

## 🍓 **Ejercicio 3**

Hacer un programa que pregunte por el radio de una esfera en centimetros y luego imprima la superficie y volumen de esta.

**PD:** _Denuevo da igual que valor se use para 𝝅, yo usé 3.141_

<br/>

## 🍓 **Ejercicio 4**

---
### Para este ejercicio por falta de pasar el contenido de estructuras de control se hará uso del metodo _**find**_ de strings, pequeña descripción y una referencia más abajo, además dejare algo parecido para le metodo _**substr**_, por si alguien quisiese hacerlo de manera distinta.
---

Hacer un programa que pregunte por:

* Primer nombre y apellido (Juanito Perez)
* RUT (11.111.111-1)
* Fecha de nacimiento (Agosto 1999)

**Ojo:** _Asuma que se ingresan los datos con el formato que esta entre parentesis._

Luego imprima una string correspondiente a como lo hubiesemos escrito en un archivo .csv via python, en este caso nos quedaria como:

```
(RUT)        (Nom y apel)  (Nacimiento)
  |               |             |
11.111.111-1,Juanito_Perez,Agosto_1999
```

**PD:** _El separador da igual cual se use pero si se va a cambiar ojo con los puntos y guion del RUT_

<br/>

# 🍓 **Referencias**

**cmath**
* https://cplusplus.com/reference/cmath/
* https://www.programiz.com/cpp-programming/library-function/cmath

**#define**
* https://cplusplus.com/doc/tutorial/preprocessor/

**const -data type-**
* https://learn.microsoft.com/en-us/cpp/cpp/const-cpp?view=msvc-170
     
<br/>

## std::string.substr(a, b)

### INPUT

* Siendo 'a' el indice del primer caracter desde donde quiere ser copiada la string y 'b' la extension de la substring.

### OUTPUT

* Se retorna una string (substring de la string original).

[Más info](https://cplusplus.com/reference/string/string/substr/)

## std::string.find(a, b) --> Hay mas argumentos opcionales

### INPUT

* Siendo 'a' la segunda string en donde se quiere buscar y 'b' desde donde empezar a buscar (si no se entrega un valor para 'b' se comienza a buscar desde el indice 0 en adelante).

### OUTPUT

* Se retorna el indice del primer caracter de la string encontrada.

[Más info](https://cplusplus.com/reference/string/string/find/)
              