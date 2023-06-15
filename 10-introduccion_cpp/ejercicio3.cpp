#include <iostream>

using namespace std;

int main(){
    int num, resultado;
    cout << "Ingrese numero: "; cin >> num;
    resultado = 0;
    while(num > 0){
        if ((num % 10) % 2 != 0)
            resultado += num % 10;
        num = num / 10;
    }
    cout << resultado << endl;
    return EXIT_SUCCESS;
}