#include <iostream>
#include <cmath>

#define PI 3.141

using namespace std;

int main()
{
    float radio;
    cout << "Radio de circunferencia: "; 
    cin >> radio;

    float perimetro, area;
    perimetro = 2 * PI * radio;
    area = PI * pow(radio, 2);

    cout << "El perimetro de la circunferencia es " << perimetro; 
    cout << ", por otro lado el area es " << area << endl;
    return 0;
}
