def f(x: int) -> None:
    if (x % 2 == 0):
        print('_', end='')
    else:
        print('*', end='')
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
