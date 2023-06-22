#include <iostream>

using namespace std;

void printArr(int arr[], u_int size);
void sortArr(int arr[], u_int size);

int main() {
    u_int size;
    size = 9;
    int arr[] = {10, 4, 15, 8, 10, 2, -8, 50, 0};
    cout << "Array: " << endl;
    printArr(arr, size);
    sortArr(arr, size);
    cout << "Sorted array: " << endl;
    printArr(arr, size);
    return EXIT_SUCCESS;
}

void sortArr(int arr[], u_int size) {
    u_int i, j;
    int aux;
    for (i = 0; i < size; i++)
        for (j = 0; j < (size - 1) - i; j++)
            if (arr[j] > arr[j + 1]) {
                aux = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = aux;
            }
}

void printArr(int arr[], u_int size) {
    u_int i;
    for (i = 0; i < size; i++)
        cout << arr[i]<<' ';
    cout << endl;
}
