#include <iostream>

using namespace std;

void printArr(int arr[], u_int size);
void eliminaImpares(int arr[], u_int size);

int main() {
    u_int size;
    size = 6;
    int arr[] = {1, 2, 3, 4, 5, 6};
    cout << "Array: " << endl;
    printArr(arr, size);    
    eliminaImpares(arr, size);
    cout << "Array: " << endl;
    printArr(arr, size);
    return EXIT_SUCCESS;
}

void eliminaImpares(int arr[], u_int size) {
    u_int i, cont;
    cont = 0;
    for (i = 0; i < size; i++)
        if (arr[i] % 2 != 0) {
            arr[i] = -1;
            cont++;
        }
    cout << "== Fueron reemplazadas "<<cont<<" posiciones del arreglo. ==" << endl;
}

void printArr(int arr[], u_int size) {
    u_int i;
    for (i = 0; i < size; i++)
        cout << arr[i]<<' ';
    cout << endl;
}
