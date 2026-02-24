#include <iostream>
#include <cmath>
#include <algorithm>

int findd(int n) {
    int fnd = 0;
    int m = 0;
    int nd;
    for (int d = 1; d < std::floor(std::sqrt(n)) + 1; d++) {
        if (n % d == 0) {
            if (d % 2 == 1) {
                fnd++;
                m = std::max(m, d);
            }
            if (d * d != n) {
                nd = n / d;
                if (nd % 2 == 1) {
                    fnd++;
                    m = std::max(m, nd);
                }
            }
            if (fnd > 5) {
                return 0;
            }
        }
    }
    if (fnd == 5) {
        return m;
    }
    return 0;
}

int main() {
    for (int n = 55000000; n <= 60000000; n++) {
        int del = findd(n);
        if (del != 0) {
            std::cout << n << ' ' << del << '\n';
        }
    }
    return 0;
}