def determinar_signo_zodiacal(signos: dict, fecha_de_nacimiento: tuple) -> str:
    """
    Recibe diccionario con signos zodiacales y sus respectivos rangos
    (signos) ademas de una fecha de nacimiento (fecha_de_nacimiento) que
    esta almacenada en una tupla con el formato (year|month|day), se 
    retorna cual es el signo zodiacal correspondiente a esa fecha de
    nacimiento en un dato de tipo string.
    """
    for signo_zodiacal in signos:
        inicio_signo = signos[signo_zodiacal][0]
        fin_signo = signos[signo_zodiacal][1]
        if ((fecha_de_nacimiento[1] == inicio_signo[0]
            or fecha_de_nacimiento[1] == fin_signo[0])
            and (fecha_de_nacimiento[2] >= inicio_signo[1]
            or fecha_de_nacimiento[2] <= fin_signo[1])):
            return signo_zodiacal


def main():
    signos = {'Aries':       ((3, 21), (4, 20)),
              'Tauro':       ((4, 21), (5, 21)),
              'Geminis':     ((5, 22), (6, 21)),
              'Cancer':      ((6, 22), (7, 23)),
              'Leo':         ((7, 24), (8, 23)),
              'Virgo':       ((8, 24), (9, 23)),
              'Libra':       ((9, 24), (10, 23)),
              'Escorpio':    ((10, 24), (11, 22)),
              'Sagitario':   ((11, 23), (12, 21)),
              'Capricornio': ((12, 22), (1, 20)),
              'Acuario':     ((1, 21), (2, 19)),
              'Piscis':      ((2, 20), (3, 20))}
    year_de_nacimiento = int(input("Año de nacimiento: "))
    month_de_nacimiento = int(input("Mes de nacimiento: "))
    day_de_nacimiento = int(input("Dia de nacimiento: "))
    fecha_de_nacimiento = (year_de_nacimiento, month_de_nacimiento,
                           day_de_nacimiento)
    print(determinar_signo_zodiacal(signos, fecha_de_nacimiento))


if __name__ == "__main__":
    main()
