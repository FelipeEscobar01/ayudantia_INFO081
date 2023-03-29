#!/usr/bin/env/python3
# -*- coding: utf-8 -*-


# Enunciado:
# Programe la funcion filtra que recibe una lista L de strings y un
# string ref con un string de referencia, y retorna una nueva lista,
# con los strings de L que cumplen con la condicion de tener una
# cantidad de vocales mayor o igual al string de referencia. Todos los
# strings estan en minusculas y sin tilde.
#
# Conclusiones:
# (1) Necesito una ~funcion filtra~
#  |_ (2) RECIBE una ~lista L de strings~.
#  |_ (3) RECIBE una ~string de referencia~.
#  |_ (4) RETORNA una ~nueva lista con aquellas strings con un 
#         numero mayor o igual de vocales que mi string de 
#         referencia~.


# (1) def filtra ........... Tengo una funcion, vacia, pero tengo (✅)
# (2) (L: list ............. Recibo una lista L (✅)
# (3) , ref: str) .......... Recibo una string ref (✅)
# (4) -> list: ............. Retorno una lista (✅)

def filtra(L: list, ref: str) -> list:
    # Creo mi nueva lista que RETORNARE.
    L_resultado = []
    # Pero ahora necesito una forma de contar las vocales de las 
    # strings que estoy recorriendo en la ~lista L~ para asi 
    # compararlas con aquellas de la ~string de referencia~.
    #
    # | Explicacion mas abajito |
    #
    # Listo, ahora guardo en una variable el numero de vocales en la
    # ~string de referencia~.
    vocales_str_de_ref = cuenta_vocales(ref)
    # Recorro la ~lista L de strings~.
    for i in L:
        # Comparo el numero de vocales que tengo en la string ubicada 
        # en el indice i de la lista L con el numero que tengo en la 
        # string ref (ya contabilizadas en la variable 
        # "vocales_str_de_ref"), evaluo si el numero de i es mayor o 
        # igual que el de ref.
        if cuenta_vocales(i) >= vocales_str_de_ref:
            # ¿¿¿ES MAYOR O IGUAL??? ... SI
            # Agrego a L_resultado la string de L con la que hice la
            # comparacion ("L[i]").
            # ¿¿¿NO LO ES??? ... NO
            # No hago nada.
            L_resultado.append(i)
    return L_resultado


# Quiero una funcion que cuente las vocales de un dato tipo string y
# retorne el conteo de estas (tipo int).

def cuenta_vocales(string: str) -> int:
    # El metodo .count() buscara dentro de toda la string que le 
    # "referenciamos" una sub-string que le entreguemos, en este caso,
    # cada vocal. (Si, cada vez recorrera la string en su totalidad 
    # buscando cada una...)
    return string.count('a') + string.count('e') + string.count('i') \
           + string.count('o') + string.count('u')
    # Otra forma de hacer este algoritmo pudiese ser:
    #
    #           vocales = "aeiou"          
    #           cantidad_de_vocales = 0     
    #           for i in range(0, len(string)):
    #               for j in range(0, len(vocales)):
    #                    if string[i] == vocales[j]:
    #                        cantidad_de_vocales += 1
    #           return cantidad_de_vocales
    #
    # Pero hay multiples formas en realidad, algunas mas o menos
    # pythonescas, la mostrada lo es menos.
    

def main():
    print(filtra(["hola", "Juan", "Andrea", "Marcelo", "Yun", "Jazz"], 
         "pato"))

    # Retorna ["hola", "Juan", "Andrea", "Marcelo"]

    print(filtra(["ola", "paralelepipedo", "alegria", "taza", "ozono",
         "Carolina"], "cabezon"))

    # Retorna ["paralelepipedo", "alegria", "ozono", "carolina"]


if __name__ == "__main__":
    main()
