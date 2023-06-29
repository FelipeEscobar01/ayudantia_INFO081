#include <iostream>
#include <string>

using namespace std;

int contarDigitos(string palabra);
bool esVocal(char search_for);
int contarVocales(string palabra);

int main() {
    string palabra;
    int digitos, vocales;

    // Recibo palabra
    cout << "Palabra?\n> "; getline(cin, palabra);
    // Guardo lo que me retorne la funcion y lo imprimo
    digitos = contarDigitos(palabra);
    cout << "Numero de digitos en la palabra: "<<digitos << endl;
    // Guardo lo que me retorne la funcion y lo imprimo
    vocales = contarVocales(palabra);
    cout << "Numero de vocales en la palabra: "<<vocales << endl;

    return EXIT_SUCCESS;
}

int contarDigitos(string palabra) {
    int cont, i;

    // Inicio contador
    cont = 0;
    // Imprimo la palabra
    cout << palabra << endl;
    // Recorro la palabra
    for(i = 0; i < palabra.length(); i++)
        // https://cplusplus.com/reference/cctype/isdigit/
        if(isdigit(palabra[i])) {
            // Es un digito! imprimo un asterisco y incremento contador
            cout << '*';
            cont++;
        }
        else
            // No es un digito, solo imprimo un espacio en blanco
            cout << ' ';
    // Imprimo un salto de linea para no tener problemas con otras impresiones
    cout << endl;

    // Retorno el contador
    return cont;
}

bool esVocal(char search_for) {
    // Creo un arreglo con las vocales
    char vocales[] = {'a', 'e', 'i', 'o', 'u'};
    // Mantengo un entero 'i' para recorrer el arreglo
    int i;
    i = 0;
    // Mientras no me salga del arreglo y la vocal que esta en la casilla 'i'
    // sea distinta de que busco, incrementa 'i'
    while(i < 5 && vocales[i] != search_for)
        i++;
    // Me sali del arreglo y en ningun momento se encontro en las vocales el
    // caracter que le entregue a la funcion, por tanto, no es vocal
    if (i == 5)
        return false;

    // El ciclo while termino por que se encontro el caracter que le entregue
    // a la funcion en el arreglo vocales! retorno true
    return true;
}

int contarVocales(string palabra) {
    // La misma idea que con contarDigitos()
    int cont, i;
    cont = 0;
    cout << palabra << endl;
    for(i = 0; i < palabra.length(); i++)
        if(esVocal(palabra[i])) {
            cout << '*';
            cont++;
        }
        else
            cout << ' ';
    cout << endl;
    return cont;
}