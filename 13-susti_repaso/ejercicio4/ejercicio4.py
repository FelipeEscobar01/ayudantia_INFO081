def escribe_mensajes(msgs: dict) -> None:
    horas = []
    for key in msgs:
        for tupla in msgs[key]:
            horas.append((int(tupla[0].replace(tupla[0][2], '')),
                          f"{key.upper()}: {tupla[1]}\n"))
                          
    horas.sort()
    print(horas)
    try:
        with open("mensajes_ordenados.txt", 'x') as archivo:
            for hora in horas:
                archivo.write(hora[1])
    except FileExistsError:
        print("El archivo \"mensajes_ordenados.txt\" ya existe en el directorio!")
        return

def recupera_mensajes(n_archivo: str) -> dict:
    msgs = {}
    try:
        with open(n_archivo, 'r') as archivo:
            for line in archivo:
                info = line.strip().split('/')
                try:
                    msgs[info[1]].append((info[0], info[2]))    
                except KeyError:
                    msgs[info[1]] = [(info[0], info[2])]
    except FileNotFoundError:
        print(f"El archivo \"{n_archivo}\" no existe en el directorio!")
    return msgs

def main():
    msgs = recupera_mensajes("mensajes.txt")
    escribe_mensajes(msgs)

if __name__ == "__main__":
    main()