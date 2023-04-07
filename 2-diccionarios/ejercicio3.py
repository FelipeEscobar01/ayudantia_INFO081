def detecta_conflictos(ramos_inscritos: list, asignaturas: dict) -> tuple:
    """
    Recibe ramos inscritos de un estudiante y el diccionario que
    contiene los horarios de todos los ramos existentes, retorna una tupla
    con los horarios en el que el estudiante tiene topes de horario
    """
    conflictos = []
    # Genera todas las combinaciones de ramos distintos (sin repetir),
    # y obtiene los conflictos invocando a la función correspondiente.
    for i in range(len(ramos_inscritos)):
        for j in range(i + 1, len(ramos_inscritos)):
            conflictos.extend(list(horarios_de_tope(asignaturas,
                                                    ramos_inscritos[i],
                                                    ramos_inscritos[j])))
    # Pasa a set para evitar duplicados, luego a tupla para retornar.
    return tuple(set(conflictos)) 
    

def horarios_de_tope(asignaturas: dict, asig1: str, asig2: str) -> tuple:
    """
    Recibe diccionario de asignaturas y dos asignaturas en concreto, 
    ambas en tipo de dato string, retorna tupla con horarios de tope
    entre las dos asignaturas
    """
    # Pasa lista de horariros a set para luego hacer la intersección.
    horarios_asig1 = set(asignaturas[asig1])
    horarios_asig2 = set(asignaturas[asig2])
    return tuple(horarios_asig1 & horarios_asig2)

def main():
    asignaturas = {'INFO081': ['LU2', 'JU1'],
                   'BAIN075': ['MA1', 'JU1'],
                   'BAIN079': ['MA1', 'JU1'],
                   'BAIN077': ['LU1', 'MI2'],
                   'INFO088': ['VI1', 'MI3'],
                   'BAIN067': ['VI2', 'MI1'],
                   'BAIN065': ['VI1', 'MI4']}
    estudiantes = {'Juan Perez': ['INFO081', 'INFO088', 'BAIN075', 'BAIN065'],
                   'Claudia Benavides': ['BAIN067', 'BAIN065', 'INFO088'],
                   'Xavi del Escoval': ['BAIN077', 'BAIN075', 'INFO081'],
                   'Bastian Gajardo': ['BAIN077', 'BAIN079', 'INFO088'],
                   'Jorge Maturana': ['INFO088', 'INFO081', 'BAIN077'],
                   'Josefina Vergara': ['BAIN079', 'BAIN065', 'BAIN075']}
    for student in estudiantes:
        print("Conflictos de " + student + ':')
        print(detecta_conflictos(estudiantes[student], asignaturas))
    
if __name__ == "__main__":
    main()
