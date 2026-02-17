#include <iostream>

bool check_a(int a) {
    for (int x = 1; x <= 100000; x++) {
        for (int y = 1; y <= 100000; y++) {
            if (!((78125 != y + 4 * x) || (a > x) && (a > y))) {return false;}
        }
    }
    return true;
}

int main(void) {
    for (int a = 1; a < 100000; a++) {
        if (check_a(a)) {
            std::cout << a;
            break;
        }
    }
    return 0;
}