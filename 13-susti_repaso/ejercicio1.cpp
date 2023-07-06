#include <iostream>
#include <vector>
#include <string>

#define TEST 1

using namespace std;

void printStringVector(vector<string> vec, char separador = ' ');
vector<string> split(string str);

int main() {
    printStringVector(split("olis q tal"));
    return 0;
}

vector<string> split(string str) {
    vector<string> a_retornar;
    int inicio, fin;
    str += ' '; // Asi la ultima palabra tambien se incluye en "a_retonar"
    inicio = 0;
    fin = str.find(' ', inicio); // Busca la primera aparicion de ' ' desde "inicio"
    while (fin != str.npos) { // Mientras se encuentre un ' ' en "str"
        /* Recordar que, el metodo "substr()" de strings toma como parametros el
        punto de inicio y el largo de la substring, no el final, el largo */
        a_retornar.push_back(str.substr(inicio, fin - inicio));
        inicio = fin + 1; // "inicio" esta una posicion mas adelante del espacio encontrado
        fin = str.find(' ', inicio); // Busco la siguiente aparicion de ' '
    }
    if (TEST) {
        cout << "---->\nSalida de split(): " << endl;
        printStringVector(a_retornar, '|');
        cout << "<----" << endl;
    }
    return a_retornar;
}

void printStringVector(vector<string> vec, char separador) {
    // Es como printear una matriz
    unsigned int i, j;
    for (i = 0; i < vec.size(); i++) {
        for (j = 0; j < vec[i].size(); j++)
            cout << vec[i][j];
        cout << separador;
    }
    cout << endl;
}