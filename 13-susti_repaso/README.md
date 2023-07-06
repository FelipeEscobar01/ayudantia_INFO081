
## 🍓 **Ejercicio C++**

#### _**Extraido de Recuperativa C++ (2022)**_

Esto es todo un ejercicio de la prueba recuperativa, yo preferi dividirlo en partes,
se debe ir reciclando las funciones mientras se avanza.

### _Parte 1:_

Lo pedido:
```
Por ejemplo, si el mensaje (contenido en un string) es “ANA RUIZ DETECTADA”, el programa debe codificarlo de la siguiente forma:
La función split recibe el string y devuelve un vector<string> separando las palabras donde exista espacio. De esta forma, para el string de ejemplo se retorna un vector con el contenido {“ANA”, “RUIZ”, “DETECTADA”}
```

Ejemplo de ejecucion:
```
---->
Salida de split(): 
olis|q|tal|
<----
olis q tal 
```

### _Parte 2:_

Lo pedido:
```
La función code, que recibe el vector<string> generado por split, devuelve un segundo vector<string>, con las palabras codificadas de acuerdo a la siguientes reglas:
Si la cantidad de letras en la palabra es par, entonces, se reemplaza la primera letra por la siguiente del alfabeto, la segunda por la subsiguiente y así sucesivamente. Por ejemplo, la palabra “RUIZ” se transforma en “SWLD”, porque R+1=S, U+2=W, I+3=L y Z+4=D
Note que al llegar a un extremo del abecedario, debe reiniciarse el mismo, de tal forma que la letra siguiente a la Z es la A, y la anterior a la A es la Z:
…RSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJK…
Si la cantidad de letras en la palabra es impar, entonces, se procede de manera similar, salvo que el reemplazo es hacia atrás. Por ejemplo, la palabra “ANA” se transforma en “ZLX” porque A-1=Z, N-2=L y A-3=X.
```

Ejemplo de ejecucion con _"olis q tal"_:
```
nkhr|r|ubm|
```

### _Parte 3:_

Lo pedido:
```
La función merge, que recibe el vector<string> generado por code, restituye los espacios entre las palabras y retorna un string con el mensaje codificado, en este caso “ZLX SWLD CCQAXNTVR”
```

Ademas sugiero un desafio extra que es desencriptar el mensaje!

Ejemplo de ejecucion con _"olis q tal"_:

(No hay, es volver a _"olis q tal"_ (si se hace el desafio, sino el dato encriptado) en un dato de tipo string y listo :P)

## 🍓 **Ejercicios Python**

### Ejercicio 1:

#### _**Extraido de Recuperativa C++ (2022)**_

Lo pedido:
```
Algo sucedió en la aplicación de mensajería favorita de 2 amigos y todos los mensajes se han desordenado y solo queda un registro similar al siguiente:

mensajes.txt
07:01/Maria/te mejores
14:53/Fernando/bien
14:54/Fernando/gracias por
07:00/Maria/Que
14:55/Maria/No hay de que
14:52/Fernando/si, todo está
14:57/Fernando/preguntar

Cada línea contiene la hora de envío de un mensaje, el nombre del contacto a quien fue enviado el mensaje y su contenido. Todos estos campos están separados entre sí por una barra diagonal ("/"). Para tratar de reparar el daño causado en esta aplicación, se solicita implementar la función recupera_mensajes(nombre: str) que recibe un string con el nombre del archivo y retorna un diccionario cuyas claves corresponden el nombre de todos los contactos y su valor una lista de tuplas con la hora y contenido de todos los mensajes enviados a ese contacto, por ejemplo:

{'Maria': [('07:01', 'te mejores'), ('07:00', 'Que'), ('14:55', 'No hay de que')], 'Fernando': [('14:53', 'bien'), ('14:54', 'gracias por'), ('14:52', 'si, está todo'), ('14:57', 'preguntar')]}

Además, se solicita implementar la función escribe_mensajes(dicc: dict) que recibe el diccionario, debe crear un archivo de nombre llamado mensaje_ordenado.txt cuyo contenido tendrá la siguiente estructura, para cada línea: el nombre de un contacto en mayúsculas seguido  por un dos puntos (":"), seguido por el mensaje enviado ordenados por hora de envío. Además, la función debe retornar el número total de contactos procesados. Guíese por el ejemplo a continuación. Ejemplo:

mensaje_ordenado.txt
MARIA: Que
MARIA: te mejores
FERNANDO: si, todo está
FERNANDO: bien
FERNANDO: gracias por
FERNANDO: preguntar
MARIA: No hay de que
```

Cabe aclarar que mi programa para generar el archivo, genera mensajes sin sentido
alguno, pero que sirven para lo buscado a practicar por el ejercicio.

Mis archivos:

mensajes.txt
```
17:43/Maria/no he podido dormir en 2 semanas
24:45/Fernando/XD
20:49/Maria/si cache
23:22/Fernando/shiuuu
22:58/Fernando/estos mensajes no tienen sentido
07:43/Fernando/dedicare mi vida al lol
17:30/Fernando/voy a ser constituyente
10:03/Fernando/YAAAAAA
05:22/Fernando/que fome
14:10/Fernando/te voy a bloquear
21:09/Fernando/como hay tao
03:35/Maria/que pena la vd
00:02/Maria/media volaita
17:07/Fernando/la revolucion industrial y sus consecuencias han sido...
08:55/Fernando/si se
13:49/Maria/ojala te mejores!!!!
20:35/Fernando/me encanta esa bandaaa
00:24/Maria/no se jugar ajedrez eso si
04:32/Fernando/ya q vola
10:08/Fernando/KIEEE PERO COMOOOOOO
03:08/Maria/ojala te empeores...
01:07/Maria/QUEEEEEEE
```

mensajes_ordenados.txt
```
MARIA: media volaita
MARIA: no se jugar ajedrez eso si
MARIA: QUEEEEEEE
MARIA: ojala te empeores...
MARIA: que pena la vd
FERNANDO: ya q vola
FERNANDO: que fome
FERNANDO: dedicare mi vida al lol
FERNANDO: si se
FERNANDO: YAAAAAA
FERNANDO: KIEEE PERO COMOOOOOO
MARIA: ojala te mejores!!!!
FERNANDO: te voy a bloquear
FERNANDO: la revolucion industrial y sus consecuencias han sido...
FERNANDO: voy a ser constituyente
MARIA: no he podido dormir en 2 semanas
FERNANDO: me encanta esa bandaaa
MARIA: si cache
FERNANDO: como hay tao
FERNANDO: estos mensajes no tienen sentido
FERNANDO: shiuuu
FERNANDO: XD
```

### Ejercicio 2:

#### _**"Extraido de Leetcode" (No realmente)**_

Lo pedido:
```
1. Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
... You can return the answer in any order.
```

Traducido:
```
Dado una lista de enteros y un valor que conseguir dentro de esta lista, retorna el
indice de los dos numeros que lograrian llegar al valor.
```

Para hacer el ejercicio descarga la plantilla!

Ejemplo de ejecucion:
```
1.
([26, 25, 4, 15, 17, 2, 24, 25], 50)
{0: 26, 6: 24, 'suma': 50}

2.
([25, 6, 30, 25, 44, 24, 5, 36, 27, 19, 34, 21, 30, 41, 18, 8, 30], 60)
{2: 30, 12: 30, 'suma': 60}

3.
([4, 36, 6, 30, 8, 37, 24, 2, 15, 30], 60)
{1: 36, 6: 24, 'suma': 60}
```

Da igual el que se prefiera retornar o no, mientras se cumpla el desafio.