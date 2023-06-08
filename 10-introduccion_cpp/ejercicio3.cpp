#include <iostream>
#include <cmath>

#define PI 3.141

using namespace std;

int main()
{
    float radio;
    cout << "Radio de esfera en centimetros: ";
    cin >> radio;

    float superficie, volumen;
    superficie = 4 * PI * pow(radio, 2);
    volumen = 4.0 / 3 * PI * pow(radio, 3);

    cout << "La superficie de la circunferencia es " << superficie;
    cout << "[cm²], por otro lado el volumen es " << volumen << "[cm³]" << endl;
    return 0;
}
