#include <iostream>

using namespace std;

void printArr(int arr[], u_int size);
void sortArr(int arr[], u_int size);
int binarySearch(int arr[], int search_for, int start, int end);

int main() {
    u_int size0, size1, size2, i;
    size0 = 8;
    size1 = 9;
    int arr0[] = {5, 4, 3, 8, -2, 0, 10, 20};
    int arr1[] = {5, 4, 3, 8, -2, 0, 10, 20, -50};
    cout << "Arrays: " << endl;
    printArr(arr0, size0);
    printArr(arr1, size1);
    sortArr(arr0, size0);
    sortArr(arr1, size1);
    cout << "Sorted arrays: " << endl;
    printArr(arr0, size0);
    printArr(arr1, size1);
    size2 = 4;
    int search_for[] = {5, 20, 3, -5};
    cout << "Searching in arr0:" << endl;
    for (i = 0; i < size2; i++)
        cout << binarySearch(arr0, search_for[i], 0, size0) << endl;
    cout << "Searching in arr1:" << endl;
    for (i = 0; i < size2; i++)
        cout << binarySearch(arr1, search_for[i], 0, size1) << endl;
    return EXIT_SUCCESS;
}

int binarySearch(int arr[], int search_for, int start, int end) {
    if (start > end)
        return -1;
    int median;
    median = (start + end) / 2;
    if (arr[median] < search_for)
        return binarySearch(arr, search_for, median + 1, end);
    if (arr[median] > search_for)
        return binarySearch(arr, search_for, start, median - 1);
    return median;
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
