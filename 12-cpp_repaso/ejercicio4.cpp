/*
Control 5 (2022):
Escriba un programa en C++, que dado un intervalo de dos números enteros 
a y b (a <= b), definido por el usuario en el rango [10,89] (ambos incluidos) 
y un dígito d, par o cero (considere como dígitos los números del 0 al 9) 
también ingresado por el usuario, implemente una función 
secuenciaPares(int a, int b, int d) que recibe los 3 números y muestra en 
pantalla una secuencia de todos los números pares en el intervalo [a,b] cuyo 
último dígito sea distinto a d.

Realice todas las validaciones. Asuma que el usuario ingresará solamente números.
*/

#include <iostream>

using namespace std;

void secuenciaPares(int a, int b, int d);

int main() {
    int a, b, d;

    // Pido 'a' mientras-
    do {
        cout << "[?..b]\n> "; cin >> a;
    } while(a < 10 || a > 89);
    // esté fuera del intervalo [10..89].

    // Pido 'b' mientras-
    do {
        cout << "[a..?]\n> "; cin >> b;
    } while(b < a || b > 89);
    // esté fuera del intervalo [a..89].

    // Pido 'd' mientras-
    do {
        cout << "Valor para \'d\'?\n> "; cin >> d;
    } while(d < 0 || d > 9 || d % 2 != 0);
    // esté fuera del intervalo [0..9] y ademas sea impar!

    cout << "Los numeros pares que cumplen la condicion son:" << endl;

    // Llamo a la funcion.
    secuenciaPares(a, b, d);

    return EXIT_SUCCESS;
}

// ... que recibe los 3 números y muestra en pantalla una secuencia de todos 
// los números pares en el intervalo [a,b] cuyo último dígito sea distinto a d.
void secuenciaPares(int a, int b, int d) {
    // Mientras a sea menor o igual que b, incrementalo
    for(; a <= b; a++)
        if(a % 2 == 0 && a % 10 != d)
            cout << a<<' ';
    cout << endl;
    // for (; a <= b; a++)
    //     |
    // ¿Y eso? Recordar que el for se divide en 3, primero las instrucciones
    // a hacer antes de empezar, luego que validar antes y mientras, y por ultimo
    // las instrucciones a hacer en cada iteracion. Como 'a' ya esta definido
    // y ademas no lo estoy pasando por referencia a la funcion es mas practico
    // que hacer un:
    //
    // for(int i = a; i <= b; i++)
    //
    // Yo considero eso mas confuso y propenso a error.
}