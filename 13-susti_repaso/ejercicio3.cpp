#include <iostream>
#include <vector>
#include <string>

using namespace std;

// -- RECICLADO EJ. ANTERIOR -->
void printStringVector(vector<string> vec, char separador = ' ');
vector<string> split(string str);
char swapEven(char &car);
char swapOdd(char &car);
vector<string> code(string str);
// <----
string merge(vector<string> pals);
vector<string> decode(string str);

int main() {
    cout << merge(decode(merge(code("olis q tal")))) << endl;
    return 0;
}

vector<string> decode(string str) {
    vector<string> pals = split(str);
    unsigned int i, j;
    for (i = 0; i < pals.size(); i++) {
        if (!(pals[i].size() % 2 == 0)) // Si el largo de pals[i] NO es par
            for (j = 0; j < pals[i].size(); j++)
                swapEven(pals[i][j]);
        else // Si ES par el largo de pals[i]
            for (j = 0; j < pals[i].size(); j++)
                swapOdd(pals[i][j]);
    }
    return pals;
}

string merge(vector<string> pals) {
    string a_retornar;
    unsigned int i;
    a_retornar = "";
    for (i = 0; i < pals.size() - 1; i++)
        a_retornar += pals[i] + " ";
    a_retornar += pals[i];
    return a_retornar;
}

// -- RECICLADO EJ. ANTERIOR -->
vector<string> code(string str) {
    vector<string> pals = split(str);
    unsigned int i, j;
    for (i = 0; i < pals.size(); i++) {
        if (pals[i].size() % 2 == 0) // Si el largo de pals[i] es par
            for (j = 0; j < pals[i].size(); j++)
                swapEven(pals[i][j]);
        else // Si no es par el largo de pals[i]
            for (j = 0; j < pals[i].size(); j++)
                swapOdd(pals[i][j]);
    }
    return pals;
}

/* Mirar la tabla ASCII, si estoy en Z y sumo, llego a un caracter, no una letra 
 (Si, tecnicamente igual es un caracter, pero se entiende), lo mismo cuando estoy
 en A y resto */
char swapOdd(char &car) {
    if (car == 'Z') return 'A';
    if (car == 'z') return 'a';
    car++;
    return car;
}

char swapEven(char &car) {
    if (car == 'A') return 'Z';
    if (car == 'a') return 'z';
    car--;
    return car;
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
    return a_retornar;
}
// <----