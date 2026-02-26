#include <iostream>

bool checkA(int a) {
    for (int x = 1; x <= 100000; x++) {
        for (int y = 1; y <= 100000; y++) {
            if (!((y < a) && (x < a) || (89241 < 5*y + x))) return false;
        }
    }
    return true;
}

int main(void) {
    for (int a = 1; a < 100000; a++) {
        if (checkA(a)) {
            std::cout << a;
            break;
        }
    }
}