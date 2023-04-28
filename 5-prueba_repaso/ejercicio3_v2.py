
def extrae_digito(n: str, d: str) -> int:
   return int(n.replace(d, '')) # Reemplaza las apariciones de d en la
                                # string 'n' por un espacio vacio, no
                                # en blanco, vacio, luego transforma
                                # la salida de esto en int.


def dibuja_rectAngulo(n: int) -> None:
   # ¿Por qué es int(max(str(n)))?
   #  Necesito transformar el entero 'n' a una string 'n' para
   #  asi poder usar el max y min, estos buscan entre distintos
   #  valores cual es el mayor, VALORES, 'n' es solo un numero,
   #  en cambio cuando uso str(n) ahora n es:
   #         
   #  n => 85342
   #  n[0] => ??? ERROR ???
   #  n = str(n) => "85342"
   #  n[0] => 8, n[1] => 5, ... , n[4] => 2
   #
   #  Despues lo vuelvo a entero para poder almacenar el numero que
   #  se haya encontrado como 'max' o 'min' dentro de la string, en las
   #  variables como un entero y no como un caracter de la string.
   base = int(max(str(n)))      # Saco el maximo entre los valores.
   altura = int(min(str(n)))    # Saco el minimo entre los valores.
   print(f"Dibujo rectángulo de {altura} x {base}")
   for i in range(altura):
       if (i == 0 or i == altura - 1):  # Para imprimir la primera y
           print('*' * base)            # ultima linea del rectangulo.
       else:
           print('*' + ' ' * (base - 2) + '*')

  
def main():
   # Recordar que el dato que input() expulsa es un dato de tipo str, 
   # esta mal poner str(input()), es redundante.
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
