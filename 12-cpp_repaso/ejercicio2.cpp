/*
Control 6 (2022):
Implemente las siguientes funciones.
borraMaximo
    Que recibe un arreglo de enteros y un entero con el largo del arreglo, 
    encuentra el mayor valor en él, retorna ese valor y en el arreglo reemplaza 
    el valor máximo encontrado por cero (0).
muestraArreglo
    Que recibe un arreglo de enteros y un entero con el largo del arreglo, y lo 
    despliega por pantalla.
*/

#include <iostream>

using namespace std;

int borraMaximo(int arr[], int tam);
void muestraArreglo(int arr[], int tam);

int main() {
    // Creo el arreglo.
    int tam, i;
    int arr[] = {15, 83, 92, 36, 12, 49, 52, 66, 64, 81, 11, 23, 47, 36};
    tam = 14;

    // Llamo a la funcion.
    for(i = 0; i < 3; i++) {
        muestraArreglo(arr, tam);
        cout << "Se borró arr "<<borraMaximo(arr, tam)<<'.' << endl;
        muestraArreglo(arr, tam);
        cout << endl;
    }

    return EXIT_SUCCESS;
}

// ... Que recibe un arreglo de enteros y un entero con el largo del arreglo, 
// encuentra el mayor valor en él, retorna ese valor y en el arreglo reemplaza 
// el valor máximo encontrado por cero (0).
int borraMaximo(int arr[], int tam) {
    int mayor, pos_mayor, i;

    // Defino como el elemento mayor al primer elemento del arreglo.
    mayor = arr[0];
    pos_mayor = 0;
    
    // Empiezo desde el segundo elemento del arreglo a buscar si hay un
    // elemento mayor a aquel definido como mayor anteriormente.
    for(i = 1; i < tam; i++)
        if(arr[i] > mayor) {
            // ES MAYOR! Lo defino como mayor y guardo la posicion en donde se
            // encuentra en el arreglo.
            mayor = arr[i];
            pos_mayor = i;
        }

    // Ahora que ya se con certeza donde se encuentra el mayor elemento del
    // arreglo lo reemplazo por un 0.
    arr[pos_mayor] = 0;
    return mayor;
}

// ... Que recibe un arreglo de enteros y un entero con el largo del arreglo, y 
// lo despliega por pantalla.
void muestraArreglo(int arr[], int tam) {
    int i;
    for(i = 0; i < tam; i++)
        cout << arr[i]<<' ';
    cout << endl;
}