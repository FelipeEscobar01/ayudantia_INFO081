## 🍉 **Ejercicio 1**

Haga la tabla de ejecución del siguiente codigo:

```
def f(x: int) -> None:
    if (x % 2 == 0):
        print('_', end=' ')
    else:
        print('*', end=' ')
    def g():
        nonlocal x
        x -= 1 
    g()
    def h():
        global y
        y = x
    h()


y = 3
x = 2
print("Dormi mas de 2 horas\n\(", end ='')
while (y > 0):
    f(y)
print(")/")
```

<br/>

## 🍉 **Ejercicio 2**

Haga la tabla de ejecución del siguiente codigo:

```
def f(z = 2) -> None:
    if (x): 
        print(llaves[x - 1], end='')
        for i in range(0, z):
            print(diccionario[llaves[x - 1]][i], end='')
    def g():
        global y
        y.pop()
    g()
    def h():
        global x
        x += 1 
    h()


diccionario = {
        '\\' : ['_', '('],
        '-' : ['.', '-'],
        ')' : ['_', '/']
}
llaves = list(diccionario.keys())
z = 0
y = ['-', '-', '-']
x = 1 
print("Aqui meditando...")
while (len(y)):
    f()
```