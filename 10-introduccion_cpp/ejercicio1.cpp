#include <iostream>
#include <string>

using namespace std;

int main(){
    string palabra;
    int mediana, i;
    cout << "Ingrese palabra: "; cin >> palabra;
    mediana = palabra.length() / 2;
    for (i = 0; i < mediana; i++)
        swap(palabra[i], palabra[(palabra.length() - i) - 1]);
    cout << palabra << endl;
    return EXIT_SUCCESS;
}