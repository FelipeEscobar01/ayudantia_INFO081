
## 🍓 **Ejercicio 1**

Imprima cuantos digitos y vocales tiene una palabra u oracion de la siguiente forma:

```
Palabra?
> H0y d0rm1 much0, m3 p4s3 cr30 j3j3j3...
H0y d0rm1 much0, m3 p4s3 cr30 j3j3j3...
 *   *  *     *   *  * *   **  * * *   
Numero de digitos en la palabra: 12
H0y d0rm1 much0, m3 p4s3 cr30 j3j3j3...
           *                           
Numero de vocales en la palabra: 1
```

## 🍓 **Ejercicio 2**

#### _**Extraido de Control 6 (2022)**_

Lo pedido:
```
Implemente las siguientes funciones.
borraMaximo
    Que recibe un arreglo de enteros y un entero con el largo del arreglo, 
    encuentra el mayor valor en él, retorna ese valor y en el arreglo reemplaza 
    el valor máximo encontrado por cero (0).
muestraArreglo
    Que recibe un arreglo de enteros y un entero con el largo del arreglo, y lo 
    despliega por pantalla.
```

Ejemplo de ejecucion:
```
15 83 92 36 12 49 52 66 64 81 11 23 47 36 
Se borró arr 92.
15 83 0 36 12 49 52 66 64 81 11 23 47 36 

15 83 0 36 12 49 52 66 64 81 11 23 47 36 
Se borró arr 83.
15 0 0 36 12 49 52 66 64 81 11 23 47 36 

15 0 0 36 12 49 52 66 64 81 11 23 47 36 
Se borró arr 81.
15 0 0 36 12 49 52 66 64 0 11 23 47 36 
```

## 🍓 **Ejercicio 3**

#### _**Extraido de Prueba 3 (2022)**_

Lo pedido:
```
    ImhotepSort se implementa en una función de C++ del mismo nombre, la cual 
recibe por referencia un arreglo a de enteros positivos 
(en cualquier orden), el largo l del arreglo, y modifica este array para 
que quede ordenado como una pirámide.
    Al finalizar la ejecución de la función ImhotepSort, el menor valor del 
arreglo debe quedar en la primera posición (0) del arreglo, el segundo menor 
en la última posición (l-1), el tercero menor en la segunda posición (1), el 
cuarto menor en la posición l-2 y así sucesivamente, alternando el extremo y 
acercándose hacia el centro.
    En caso que existan valores repetidos, estos se tratarán de manera 
independiente.
```

Ejemplo de ejecucion:
```
7 3 4 1 2 8 3 4 3 
1 3 3 4 8 7 4 3 2 
```

## 🍓 **Ejercicio 4**

#### _**Extraido de Control 5 (2022)**_

Lo pedido:
```
Escriba un programa en C++, que dado un intervalo de dos números enteros 
a y b (a <= b), definido por el usuario en el rango [10,89] (ambos incluidos) 
y un dígito d, par o cero (considere como dígitos los números del 0 al 9) 
también ingresado por el usuario, implemente una función 
secuenciaPares(int a, int b, int d) que recibe los 3 números y muestra en 
pantalla una secuencia de todos los números pares en el intervalo [a,b] cuyo 
último dígito sea distinto a d.

Realice todas las validaciones. Asuma que el usuario ingresará solamente números.
```

Ejemplo de ejecucion:
```
[?..b]
> 10
[a..?]
> 89
Valor para 'd'?
> 0
Los numeros pares que cumplen la condicion son:
12 14 16 18 22 24 26 28 32 34 36 38 42 44 46 48 52 54 56 58 62 64 66 68 72 74 76 78 82 84 86 88 
```

# **Plantillas propuestas**

**ejercicio1.cpp**
```
#include <iostream>
#include <string>

using namespace std;

int contarDigitos();
bool esVocal();
int contarVocales();

int main() {
    return EXIT_SUCCESS;
}

int contarDigitos() {
    return -1;
}

bool esVocal() {
    return false;
}

int contarVocales() {
    return -1;
}
```

**ejercicio2.cpp**
```
#include <iostream>

using namespace std;

int borraMaximo();
void muestraArreglo();

int main() {
    return EXIT_SUCCESS;
}

// ... Que recibe un arreglo de enteros y un entero con el largo del arreglo, 
// encuentra el mayor valor en él, retorna ese valor y en el arreglo reemplaza 
// el valor máximo encontrado por cero (0).
int borraMaximo() {
    return -1;
}

// ... Que recibe un arreglo de enteros y un entero con el largo del arreglo, y 
// lo despliega por pantalla.
void muestraArreglo() {
}
```

**ejercicio3.cpp**
```
#include <iostream>

using namespace std;

void Imhotepsort();
int posicionMinimo();
void muestra();

int main() {
    return EXIT_SUCCESS;
}

void Imhotepsort() {
}

int posicionMinimo() {
    return -1;
}

void muestra() {
}
```

**ejercicio4.cpp**
```
#include <iostream>

using namespace std;

void secuenciaPares();

int main() {
    return EXIT_SUCCESS;
}

void secuenciaPares() {
}
```