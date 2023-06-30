/*
Prueba 3 (2022):
    ImhotepSort se implementa en una función de C++ del mismo nombre, la cual 
recibe por referencia un arreglo a de enteros positivos 
(en cualquier orden), el largo l del arreglo, y modifica este array para 
que quede ordenado como una pirámide.
    Al finalizar la ejecución de la función ImhotepSort, el menor valor del 
arreglo debe quedar en la primera posición (0) del arreglo, el segundo menor 
en la última posición (l-1), el tercero menor en la segunda posición (1), el 
cuarto menor en la posición l-2 y así sucesivamente, alternando el extremo y 
acercándose hacia el centro.
    En caso que existan valores repetidos, estos se tratarán de manera 
independiente.
*/

#include <iostream>

using namespace std;

void Imhotepsort(int arr[], int tam);
int posicionMinimo(int arr[], int ini, int fin);
void muestra(int arr[], int tam);

int main() {
    // Creo el arreglo.
    int tam;
    int arr[] = {7, 3, 4, 1, 2, 8, 3, 4, 3};
    tam = 9;

    // Llamo a la funcion.
    muestra(arr, tam);
    Imhotepsort(arr, tam);
    muestra(arr, tam);

    return EXIT_SUCCESS;
}

void Imhotepsort(int arr[], int tam) {
    int ini, fin, i;
    
    // Declaro el sector del arreglo en donde voy a trabajar.
    ini = 0;
    fin = tam - 1;

    // Uso 'i' ya que necesito alternar entre el inicio y fin del arreglo
    // i % 2 == 0? (Si) Inicio : (No) Fin
    i = 0;

    // Ok, no es literalmente esto pero en resumen. Mientras el rango en el que
    // estoy trabajando abarque un elemento o mas, hacer-
    while(ini <= fin) {
        if(i % 2 == 0) {

            // Intercambio el elemento del inicio con el menor elemento del
            // intervalo.
            swap(arr[ini], arr[posicionMinimo(arr, ini, fin)]);

            // Ahora como el elemento del inicio es el final cierro el intervalo
            // por el inicio.
            ini++;

        } else {
            // Intercambio el elemento del final con el menor elemento del
            // intervalo.
            swap(arr[fin], arr[posicionMinimo(arr, ini, fin)]);
            // Ahora como el elemento del final es el final cierro el intervalo
            // por el final (Si, mucho final).
            fin--;
        }
        // Para que cambie de if -> else o de else -> if.
        i++;
    }
}

int posicionMinimo(int arr[], int ini, int fin) {
    int pos, menor;
    // Defino como el elemento menor del arreglo al primero de este.
    pos = ini;
    menor = arr[pos];
    // Empiezo desde el segundo elemento del arreglo buscando un elemento que
    // sea menor al ya definido, y si es asi, que sea menor al nuevo, asi hasta
    // el final del arreglo.
    for(ini++; ini <= fin; ini++)
        if(arr[ini] < menor) {
            // ES MENOR! Guardo su valor y posicion, el valor para compararlo
            // con los elementos que sigan del arreglo, si siguiesen.
            menor = arr[ini];
            pos = ini;
        }
    return pos;
}

void muestra(int arr[], int tam) {
    int i;
    for(i = 0; i < tam ; i++)
        cout << arr[i]<<' ';
    cout << endl;
}