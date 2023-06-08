#include <iostream>

using namespace std;

int main()
{
    cout << "9 / 5 (int / int) = " << 9 / 5 << endl;
    cout << "9.0 / 5.0 (float / float) = " << 9.0 / 5.0 << endl;
    cout << "9.0 / 5 (float / int) = " << 9.0 / 5 << endl;
    cout << "9 / 5.0 (int / float) = " << 9 / 5.0 << endl;

    cout << "Ahora lo mismo pero guardando el resultado en una variable de "
         "tipo int o float." << endl;

    int tipo_int;
    cout << "ALMACENANDO EN VARIABLE DE TIPO INT:" << endl;

    tipo_int = 9 / 5;
    cout << "Caso 1: " << tipo_int << ", ";

    tipo_int = 9.0 / 5.0;
    cout << "Caso 2: " << tipo_int << ", ";

    tipo_int = 9.0 / 5;
    cout << "Caso 3: " << tipo_int << ", ";

    tipo_int = 9 / 5.0;
    cout << "Caso 4: " << tipo_int << endl;

    float tipo_float;
    cout << "ALMACENANDO EN VARIABLE DE TIPO FLOAT:" << endl;

    tipo_float = 9 / 5;
    cout << "Caso 1: " << tipo_float << ", ";

    tipo_float = 9.0 / 5.0;
    cout << "Caso 2: " << tipo_float << ", ";

    tipo_float = 9.0 / 5;
    cout << "Caso 3: " << tipo_float << ", ";

    tipo_float = 9 / 5.0;
    cout << "Caso 4: " << tipo_float << endl;

    return 0;
}
