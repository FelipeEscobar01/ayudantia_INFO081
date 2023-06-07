#include <iostream>  
                                                                             /*
            i = in (entrada), o = out (salida), stream = flujo.
  Flujo de entrada y salida, se relaciona con el namespace std: cin, cout...
                                                                             */
using namespace std;
                                                                             /*
   Toda funcion que se llame desde el programa se buscara en el namespace
  std, de esta forma me ahorro el concretar que la funcion corresponde al
                                namespace.

               std::cout ----> cout    std::cin ----> cin

    Si escribo "cout" se asume que es aquel funcion cout del namespace "std",
  lo mismo para "cin", de hecho si llegasemos a tener una funcion con el mismo
   nombre de alguna que este en std C++ es bastante inteligente en asumir cual
                    es la que se esta esperando se use.

-------------------------------------------------------------------------------

*(1) = Tipo de dato que va a retornar la funcion, ejemplos:
     int, float, double, bool, char...
*(2) = Nombre de la funcion.
*(3) = Argumentos de la funcion.

(1) (2) (3)             
 |   |   |                                                                   */
int main( )
{


    return 0; // Puede ser cualquier valor entero.
}
