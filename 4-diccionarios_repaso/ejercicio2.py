
estudiantes = {"1-1" : ("Juan", "juan@gmail.com"), 
               "2-2" : ("Claudia", "clau@uach.cl"),
               "3-3" : ("María", "mary@bla.com"),
               "4-4" : ("Andrés", "afer@hotmail.com")
              }
cursos = {"c-1" : ("Cálculo 1", 6, "Básico", []),
          "c-2" : ("Cálculo 2", 6, "Básico", ["c1"]),
          "p-1" : ("Progra 1", 6, "Básico", []),
          "p-2" : ("Progra 2", 6, "Básico", ["p-1","c-1"]),
          "bd-1" : ("Bases de Datos", 5, "Licenciatura", ["p-2","c-1"]),
          "so-1" : ("Sistemas Operativos", 5, "Licenciatura", ["p-2","bd-1"]),
          "ps-1" : ("Proyectos de Software", 6, "Profesional", ["c-2", "so-1"])
         }
matriculas = [("1-1", "c-1", 2017, 1, 2.4, "Reprobado"),
              ("1-1", "c-1", 2017, 2, 5.2, "Aprobado"), 
              ("1-1", "p-1", 2017, 1, 5.4, "Aprobado"),
              ("1-1", "p-2", 2017, 2, 6.3, "Aprobado"),
              ("1-1", "c-2", 2018, 1, 4.0, "Aprobado"),
              ("1-1", "bd-1", 2018, 1, 5.2, "Aprobado"),
              ("1-1", "so-1", 2018, 2, 3.8, "Reprobado"),
              ("2-2", "c-1", 2017, 1, 4.2, "Aprobado"),
              ("2-2", "p-1", 2017, 1, 5.6, "Aprobado"),
              ("2-2", "c-2", 2017, 2, 3.5, "Reprobado"),
              ("2-2", "p-2", 2017, 2, 4.7, "Aprobado"),
              ("2-2", "c-2", 2018, 1, 3.3, "Aprobado"),
              ("2-2", "bd-1", 2018, 1, 5.1, "Aprobado"),
              ("2-2", "so-1", 2018, 2, 4.0, "Aprobado"),
              ("2-2", "ps-1", 2018, 2, 3.2, "Reprobado"),
              ("2-2", "ps-1", 2019, 1, 6.0, "Aprobado")]


def aviso_reprobados(matriculas: list, estudiantes: dict, cursos: dict,
                     ciclo: str, anno: int, sem: int) -> tuple:
    lista_correos = []
    for resultado in matriculas: # ("1-1", "c-1", 2017, 1, 2.4, "Reprobado")
        if (resultado[2] == anno and resultado[3] == sem
            and resultado[5] == "Reprobado"
            and cursos[resultado[1]][2] == ciclo):
            mail = estudiantes[resultado[0]][1]
            if mail not in lista_correos:
                lista_correos.append(mail)
    return tuple(lista_correos)


def avance_ciclo(matriculas: list, estudiantes: dict, cursos: dict, 
                 RUT: str) -> dict:
    respuesta = {"Básico" : 0,
                 "Licenciatura" : 0,
                 "Profesional" : 0
                }
    for dato in matriculas: # ("1-1", "c-1", 2017, 1, 2.4, "Reprobado")
        if (dato[0] == RUT and dato[5] == "Aprobado"):
            for llave in respuesta:
                if (cursos[dato[1]][2] == llave):
                    respuesta[llave] += 1
    return respuesta


def main():
    print(aviso_reprobados(matriculas, estudiantes, cursos, "Básico", 2017, 1))
    print(aviso_reprobados(matriculas, estudiantes, cursos, "Profesional", 2018, 2))
    print(avance_ciclo(matriculas, estudiantes, cursos, "1-1"))
    print(avance_ciclo(matriculas, estudiantes, cursos, "2-2"))


if __name__ == "__main__":
    main()
