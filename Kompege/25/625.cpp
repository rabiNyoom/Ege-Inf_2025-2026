#include <iostream>
#include <cmath>
#include <algorithm>

int dels(int n) {
    int f = 0;
    int m = 0;
    for (int d = 2; d < std::floor(std::sqrt(n)) + 1; d++) {
        if (n % d == 0) {
            f += 1;
            m = std::max(m, d);
            if (d * d != n) {
                f += 1;
                m = std::max(m, n / d);
            }
            if (f > 3) return 0;
        }
    }
    if (f == 3) return m;
    return 0;
}

int main() {
    for (int n = 106732567; n <= 152673836; n++) {
        int r = dels(n);
        if (r != 0) {
            std::cout << n << ' ' << r << '\n';
        }
    }
    return 0;
}