#include <iostream>
/*
   I/O Stream, osea, flujo de input y output, esta relacionado con la existencia
   del namespace std en mi codigo.
            ___________
     Input  |         |  Output
      --->  |         |  ---> 
            -----------
            Mi proyecto
*/
#include <cmath> // Para tener acceso a pow(a, b).

using namespace std;
/*
   Las funciones que llame en mi programa y no haya yo definido en el mismo se
   buscaran en el namespace std, ahorrandome asi el concretar en cada ocasion
   decir donde sacar la definicion de la funcion que uso (std::cin -> cin o 
   std::cout -> cout).
*/

int main()
/*
   int main(){}
    - int, es el tipo de dato que se retornara.
    - main, nombre con que identificar y llamar a la funcion.
    - (), aqui irian los argumentos.
    - {}, dentro van las instrucciones.
*/
{
    float radio;
    cout << "Radio de circunferencia: "; 
    cin >> radio;

    const float PI = 3.141;
    float perimetro, area;
    perimetro = 2 * PI * radio;
    area = PI * pow(radio, 2);

    cout << "El perimetro de la circunferencia es " << perimetro; 
    cout << ", por otro lado el area es " << area << endl;
    return 0;
}
