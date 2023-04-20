turistas = {132 : ("Mario Vasquez", 6, 3),
            13 : ("Maria Ines Campos", 11, 4),
            58 : ("Vicente Cush", 5, 4),
            342 : ("Mario Neta", 7, 2),
            789 : ("Eliza Noriega", 7, 5),
            76 : ("Amalia Alvarez", 2, 3),
            87 : ("Adolfo Rivera", 7, 1)
            }
entretencion = [("Buceo", 5), ("Masajes", 6), ("Casino", 4), 
                ("Piscina", 7), ("Playa", 4), ("Surf", 7),
                ("Baile entretenido", 2), ("Teatro", 5), ("Restaurant", 6),
                ("Karaoke", 4), ("Bingo", 7), ("Cine", 5), 
                ("Bar", 1), ("Spa", 5), ("Gimnasio", 4), 
                ("Cabalgata", 2)]


def filtrar(entretencion: list, puntuacion: int) -> list:
    L = []
    for x in entretencion:
        if (x[1] >= puntuacion):
            L.append(x[0])
    return L


def promedio_dias(turistas: dict, entretencion: list, 
                  e: str) -> float:
    index = 0
    while (index != len(entretencion) 
           and e != entretencion[index][0]):
        index += 1
    if (index != len(entretencion)):
        suma = 0
        cont = 0
        for x in turistas: # 132
            if (turistas[x][1] == index): # 6 == index
                suma += turistas[x][2]
                cont += 1
        if (cont != 0):
            return suma / cont
        else:
            return -1
    return -1


def usuarios_por_entretencion(turistas: dict, 
                              entretencion: list) -> dict:
    user_entretencion = {}
    for x in turistas:
        for i in range(len(entretencion)):
            L = []
            if (turistas[x][1] == i):
                if (entretencion[i][0] not in user_entretencion):
                    user_entretencion[entretencion[i][0]] = [x]
                else:
                    user_entretencion[entretencion[i][0]].extend([x])
        for y in user_entretencion:
            user_entretencion[y].sort()
    return user_entretencion


def main():
    print(filtrar(entretencion, 6))
    print("Promedio:", promedio_dias(turistas, entretencion, "Teatro"))
    print("Promedio:", promedio_dias(turistas, entretencion, "Bar"))
    entretencion_personas = usuarios_por_entretencion(turistas, entretencion)
    print(entretencion_personas)



if __name__ == "__main__":
    main()
