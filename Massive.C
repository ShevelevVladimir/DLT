#include <iostream>
#include <string>

using std::cout;
using std::cin;
using std::endl;

int main()
{    
        int arr[10];

        // Заполняем массив с клавиатуры
        for (int i = 0; i < 10; i++) {
            cout << "[" << i + 1 << "]" << ": ";
            cin >> arr[i];
        }

        // И выводим заполненный массив.
        cout << "\nВаш массив: ";

        for (int i = 0; i < 10; ++i) {
            cout << arr[i] << " ";
        }

        cout << endl;

        return 0;
}
