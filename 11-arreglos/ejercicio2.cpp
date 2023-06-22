#include <iostream>

using namespace std;

void printArr(int arr[], u_int size);
bool isPrime(int num, int = 2);
void primeNumsInArr(int arr[], u_int size);

int main() {
    u_int size;
    size = 5;
    int arr[] = {1, 3, 5, 7, 6};
    cout << "Array: " << endl;
    printArr(arr, size);
    cout << "Prime numbers in array: " << endl;
    primeNumsInArr(arr, size);
    return EXIT_SUCCESS;
}

void primeNumsInArr(int arr[], u_int size) {
    u_int i;
    for (i = 0; i < size; i++)
        if (isPrime(arr[i]))
            cout << arr[i]<<' ';
    cout << endl;
}

bool isPrime(int num, int divisor) {
    if (num <= 1)
        return false;
    if (num % divisor == 0)
        return false;
    if (divisor * divisor > num)
        return true;
    return isPrime(num, divisor + 1);
}

void printArr(int arr[], u_int size) {
    u_int i;
    for (i = 0; i < size; i++)
        cout << arr[i]<<' ';
    cout << endl;
}
