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
