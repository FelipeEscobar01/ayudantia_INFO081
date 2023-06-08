#include <iostream>
#include <string>

using namespace std;

int main()
{
    /*
     
       std::string.substr(a, b)

       - INPUT:
       Siendo 'a' el indice del primer caracter desde donde quiere ser
       copiada la string y 'b' la extension de la substring.
       - OUTPUT:
       Se retorna una string (substring de la string original).

       ref: https://cplusplus.com/reference/string/string/substr/

    -----------------------------------------------------------------------
            
       std::string.find(a, b) --> Hay mas argumentos opcionales

       - INPUT:
       Siendo 'a' la segunda string en donde se quiere buscar y 'b' desde
       donde empezar a buscar (si no se entrega un valor para 'b' se comienza
       a buscar desde el indice 0 en adelante).
       - OUTPUT:
       Se retorna el indice del primer caracter de la string encontrada.

       ref: https://cplusplus.com/reference/string/string/find/
                  
    */

    string nombre_entero, rut, fecha_de_nacimiento;

    // Ej: Juanito Perez
    cout << "Ingrese su primer nombre y apellido: ";
    getline(cin, nombre_entero);

    // Ej: 11.111.111-1
    cout << "Ingrese su RUT: ";
    cin >> rut;

    cin.ignore();
    /*
       El por qué de esto es debido a, segun ChatGPT:

       "...When you use cin >> to read input from the user, it leaves a 
       newline character ('\n') in the input stream. When you then use 
       getline(cin, fecha_de_nacimiento), it reads that newline character as 
       an empty line, causing the program to terminate prematurely. To resolve 
       this, you can add cin.ignore() after cin >> rut to clear the newline 
       character from the input stream before using getline."

       Se puede evitar hacerlo siguiendo la misma logica de poner siempre
       getline pero ademas la explicacion permite entender mejor el por qué
       hablamos de "iostream".
    */

    // Ej: Agosto 1998
    cout << "Ingrese su mes y año de nacimiento: ";
    getline(cin, fecha_de_nacimiento);

    nombre_entero[nombre_entero.find(" ")] = '_';
    fecha_de_nacimiento[fecha_de_nacimiento.find(" ")] = '_';

    string a_escribir_en_csv;
    a_escribir_en_csv = rut + ',' + nombre_entero + ',' + fecha_de_nacimiento;
    cout << "Linea a escribir en el csv: " << a_escribir_en_csv << endl;
    return 0;
}
