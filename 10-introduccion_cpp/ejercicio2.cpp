#include <iostream>
#include <string>

using namespace std;

int main(){
    int size, num1, num2, i, res;
    cout << "Cuantos valores de fibonnacci se desean imprimir: "; cin >> size;
    num1 = 0;
    num2 = 1;
    i = 0;
    cout << num1 << ' ' << num2 << ' ';
    while(i++ != size - 1){
        res = num1 + num2;
        cout << res << ' ';
        num1 = num2;
        num2 = res;
    }
    cout << endl;
    return EXIT_SUCCESS;
}
