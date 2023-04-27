def extrae_digito(n: int, d: int) -> int:
   return int(str(n).replace(d, ''))


def dibuja_rectAngulo(n: int) -> None:
   numtxt = str(n)  
   base = int(max(numtxt))      # Saco el maximo entre los valores
   altura = int(min(numtxt))    # Saco el minimo entre los valores
   print(f'dibujo rectángulo de {altura} x {base}')
   for i in range(altura):
       if (i == 0 or i == altura - 1):
           print('*' * base)
       else:
           print('*' + ' ' * (base - 2) + '*')

  
def main():
   while (True):
       n = input("Ingrese un número de 5 dígitos o más: ")
       if (n.isdigit() and len(n) >= 5):
           break
       print("Error, intente de nuevo")
   while (True):
       d = input("Ingrese un número de 1 dígito: ")
       if (d.isdigit() and len(d) == 1):
           break
       print("Error, intente de nuevo")
   num = extrae_digito(n, d)
   print(str(num)[::-1])
   dibuja_rectAngulo(num)


if __name__ == "__main__":
   main()
