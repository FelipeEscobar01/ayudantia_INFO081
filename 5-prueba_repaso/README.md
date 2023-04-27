## 🍉 **Ejercicio 1**

##### **Inspiracion: Prueba Recuperativa 2022**

<br/>

Programe la funcion:

```
es_palindromo(numero: str) -> bool:
```

Recibe un numero, retorna un valor booleano correspondiente a si es o no palindromo.

Salida esperada:

```
Ingrese numero
> 444
Es 444 palindromo? True
Ingrese numero
> 432
Es 432 palindromo? False
Ingrese numero
> 432234
Es 432234 palindromo? True
Ingrese numero
>
```

<br/>

## 🍉 **Ejercicio 2**

##### **Inspiracion: Prueba Recuperativa 2022**

<br/>

Descifra cual es el mensaje escondido en el siguiente diccionario:

```
palabra = {127 : 'N', 293 : 'e', 145 : 'e',
           297 : 's', 373 : 't', 319 : 'i',
           504 : 'o', 531 : ' ', 199 : 'c',
           541 : 'd', 592 : 'o', 810 : 'á',
           679 : 'm', 664 : 'r', 712 : 'i',
           759 : 'r', 771 : ' ', 790 : 'm',
           816 : 's'}
```

Para ello programe la funcion:

```
def descifra_mensaje(palabra: dict) -> None:
```

**¡Las llaves estan desordenadas pero se necesitan ordenar de menor a mayor!**

<br/>

## 🍉 **Ejercicio 3**

##### **Fuente: Prueba Nº1 2022**

<br/>

Escriba un programa en Python que solicite el ingreso de dos números: n y d, donde n es un número entero positivo que está compuesto por 5 o más dígitos (0..9) (valide que n sea correcto) y d es un número de un dígito (0..9) (valide que d sea correcto). 

Implemente una función: 

```
def extrae_digito(n: int, d:int) -> int: 
```

La cual retorna el número generado luego de eliminar del número n todos los dígitos que son iguales a d. Muestre en pantalla el número generado en orden inverso.

Implemente una función:

```
def dibuja_rectAngulo(n: int) -> None:
```

Que dibuja los bordes de un rectángulo donde la base corresponde al dígito mayor y la altura al dígito menor. 

Por ejemplo:

```
Ingrese un número de 5 dígitos o más: dkdjsj
Error, intente de nuevo
Ingrese un número de 5 dígitos o más: 8732
Error, intente de nuevo
Ingrese un número de 5 dígitos o más: 88945694
Ingrese un número de 1 dígito: f
Error, intente de nuevo
Ingrese un número de 1 dígito: 434
Error, intente de nuevo
Ingrese un número de 1 dígito: 4
965988
Dibujo rectángulo de 5 x 9
*********
*       *
*       *
*       *
*********
```

<br/>
