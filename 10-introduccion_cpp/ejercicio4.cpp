#include <iostream>
#include <cmath>

using namespace std;

int main(){
    int opcion, flotante, i_numero1, i_numero2;
    float f_numero1, f_numero2;
    opcion = -1;
    while(true){
        // Termina el programa.
        if(opcion == 0) break;
        cout << "(1) Suma" << endl;
        cout << "(2) Resta" << endl;
        cout << "(3) Multiplicacion" << endl;
        cout << "(4) Division o division entera" << endl;
        cout << "(5) Elevar / Raiz" << endl;
        cout << "¿Que operacion quiere realizar? "; cin >> opcion;
        if(opcion > 0 && opcion < 6){
            cout << "¿Es una operacion entre flotantes? "
                 << "Si quiere usar flotantes ingrese numero != \'0\': ";
            cin >> flotante;
        }
        switch(opcion){
            case 1:
                cout << "<----" << endl;
                if(flotante){
                    cout << "Numero 1\n> "; cin >> f_numero1;
                    cout << "Numero 2\n> "; cin >> f_numero2;
                    cout << "Resultado: " << f_numero1 + f_numero2 << endl;
                }
                else{
                    cout << "Numero 1\n> "; cin >> i_numero1;
                    cout << "Numero 2\n> "; cin >> i_numero2;
                    cout << "Resultado: " << i_numero1 + i_numero2 << endl;
                }
                cout << "---->" << endl;
                break;
            case 2:
                cout << "<----" << endl;
                if(flotante){
                    cout << "Numero 1\n> "; cin >> f_numero1;
                    cout << "Numero 2\n> "; cin >> f_numero2;
                    cout << "Resultado: " << f_numero1 - f_numero2 << endl;
                }
                else{
                    cout << "Numero 1\n> "; cin >> i_numero1;
                    cout << "Numero 2\n> "; cin >> i_numero2;
                    cout << "Resultado: " << i_numero1 - i_numero2 << endl;
                }
                cout << "---->" << endl;
                break;
            case 3:
                cout << "<----" << endl;
                if(flotante){
                    cout << "Numero 1\n> "; cin >> f_numero1;
                    cout << "Numero 2\n> "; cin >> f_numero2;
                    cout << "Resultado: " << f_numero1 * f_numero2 << endl;
                }
                else{
                    cout << "Numero 1\n> "; cin >> i_numero1; 
                    cout << "Numero 2\n> "; cin >> i_numero2;
                    cout << "Resultado: " << i_numero1 * i_numero2 << endl;
                }
                cout << "---->" << endl;
                break;
            case 4:
                cout << "<----" << endl;
                if(flotante){
                    cout << "Numero 1\n> "; cin >> f_numero1;
                    cout << "Numero 2\n> "; cin >> f_numero2;
                    cout << "Resultado: " << f_numero1 / f_numero2 << endl;
                }
                else{
                    cout << "Numero 1\n> "; cin >> i_numero1;
                    cout << "Numero 2\n> "; cin >> i_numero2;
                    cout << "Resultado: " << i_numero1 / i_numero2 << endl;
                }
                cout << "---->" << endl;
                break;
            case 5:
                cout << "<----" << endl;
                if(flotante){
                    cout << "Numero\n> "; cin >> f_numero1;
                    cout << "Exponente\n> "; cin >> f_numero2;
                    cout << "Resultado: " << pow(f_numero1, f_numero2) << endl;
                }
                else{
                    cout << "Numero\n> "; cin >> i_numero1;
                    cout << "Exponente\n> "; cin >> i_numero2;
                    cout << "Resultado: " << pow(i_numero1, i_numero2) << endl;
                }
                cout << "---->" << endl;
                break;
            default:
                cout << "!!!!!" << endl;
                cout << "Operacion no valida." << endl;
                cout << "¡¡¡¡¡" << endl;
                cout << "¿Quiere salir del programa? Si quiere salir del "
                     "programa ingrese \'0\': ";
                cin >> opcion;
                break;
        }
    }
    return EXIT_SUCCESS;
}
