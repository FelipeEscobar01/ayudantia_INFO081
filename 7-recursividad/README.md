
## 🥑 **Ejercicio 1**

Escriba una funcion recursiva que me entregue el factorial de un numero

**->** _El factorial de 5 es, 5 * 4 * 3 * 2 * 1 = 120._

<br/>

## 🥑 **Ejercicio 2**

Escriba una funcion recursiva que me entregue un valor booleano correspondiente a si un numero es primo o no.

**->** _Un numero es primo si es solo divisible por si mismo y 1._

<br/>

## 🥑 **Ejercicio 3**

Escriba una funcion recursiva que me invierta una palabra, **esta funcion no tiene que retornar ni un dato, ademas, se modifica la palabra en el lugar, es decir, no se usa una copia.**

**->** _Jose ... esoJ_

<br/>

## 🥑 **Ejercicio 4**

Escriba una funcion recursiva que me entregue un valor booleano correspondiente a si una palabra es palindromo o no. 

**->** _Una palabra es palindromo si se deletrea igual en ambos sentidos._

<br/>

## 🥑 **Ejercicio 5**

Escriba una funcion recursiva que me retorne que valor de la secuencia de fibonacci corresponde aquel posicion/indice que le entregue.

**->** _La secuencia de fibonacci consiste en sumar los dos numeros anteriores empezando de 0 y 1_ 

```
fib: 0  1  1  2  3  5  8  13  21  34 ...
     |  |  |  |  |  |  |  |   |   |
     1  2  3  4  5  6  7  8   9   10 ...
```

**Visualice en un arbol la ejecucion de esta funcion, ¿como se podria optimizar el algoritmo?**
          
<br/>

## 🥑 **Ejercicio 6**

Escriba una funcion recursiva que me retorne la posicion en la que se encuentra un valor dentro de una lista, si no se encuentra retorne -1, **para el algoritmo use la busqueda binaria.**

La busqueda binaria consiste en, tengo una lista ordenada:

```
lista = [1, 4, 8, 10, 20, 50, 80, 95, 120]
```

Solo me interesa la mediana que en este caso seria:

```
mediana = len(lista) // 2
```

Pregunto tres cosas, dependiendo de la respuesta mi actuar:
* **¿Es la mediana menor al valor que busco?** Si es asi voy hacia la izquierda (donde estan los menores).
* **¿Es la mediana igual al valor que busco?** Si es asi retorno la posicion de la mediana.  
* La tercera pregunta es irrelevante supongo, a fin de cuentas **si no es menor ni igual, significa que es mayor.**

## Visualizacion:

```
Busco 1:
    
1.  --------------
                 |
    1  4  8  10  20  50  80  95  120

2.  ----
       |
    1  4  8  10

3.  -
    |
    1

SI ESTÁ

Busco 150:

1.  --------------
                 |
    1  4  8  10  20  50  80  95  120   

2.  -----
        |
    50  80  95  120

3.  -
    |    
    95  120

4.  -
    |    
    120

5.  -
    |
    ?

NO ESTÁ
```

