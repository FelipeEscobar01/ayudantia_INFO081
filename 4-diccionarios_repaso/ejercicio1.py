
def almacena_fibonacci(num: int) -> dict:
    baul = {}
    num_ant = (0, 1)
    for i in range(1, num + 1): 
        baul[i] = num_ant
        num_ant = (num_ant[1], sum(num_ant))
    return baul


def consulta_baul(baul: dict) -> None:
    while (True):
        print(f"Estan almacenados {len(baul)} valores de fibonacci")
        accede = int(input("¿A qué valor quiere acceder?\n> "))
        if (accede < 1 or accede > len(baul)):
            break 
        print(f"El fibonacci numero {accede} es {sum(baul[accede])}")
        

def main():
    num = int(input("Numero hasta el que se quiere almacenar\n> "))
    while (num <= 0):
        num = int(input("Numero hasta el que se quiere almacenar\n> "))
    baul = almacena_fibonacci(num)
    consulta_baul(baul)


if __name__ == "__main__":
    main()
