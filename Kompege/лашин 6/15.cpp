#include <iostream>

bool check_a(int a) {
    for (int x = 1; x < 500000000; x++) {
        if (!((x % 22229 == 0) <= ((x % a != 0) <= (x % 22247 != 0)))) return false;
    }
    return true;
}

int main(void) {
    for (int a = 494528565; a > 0; a--) {
        if (check_a(a)) {
            std::cout << a;
            break;
        }
    }
}