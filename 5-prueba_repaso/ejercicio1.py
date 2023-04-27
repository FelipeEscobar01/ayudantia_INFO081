
def es_palindromo(numero: str) -> bool:
    """
    Recibe un numero, retorna un valor booleano correspondiente a si 
    es o no palindromo. 
    """
    return numero == numero[::-1]
    

def main():
    while(True):
        num = input("Ingrese numero\n> ")
        if (num == ''):
            break
        else:
            print(f"Es {num} palindromo? {es_palindromo(num)}")


if __name__ == "__main__":
    main()
