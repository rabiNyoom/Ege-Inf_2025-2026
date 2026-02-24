// можно и на питоне

#include <iostream>
#include <cmath>
#include <vector>

bool isPrime(int n) {
    for (int d = 2; d < floor(sqrt(n)) + 1; d++) {
            if (n % d == 0) return false;
        }
    return true;
}

using namespace std;
vector<int> dels(int n) {
    vector<int> v;
    for (int d = 2; d < floor(sqrt(n)) + 1; d++) {
        if (n % d == 0) {
            if (isPrime(d)) v.push_back(d);
            if (d * d != n) v.push_back(n / d);
            if (v.size() > 2) return v;
        }
    }
    return v;
}

int main() {
    for (int n = 125697; n <= 125721; n++) {
        auto r = dels(n);
        if (r.size() == 2) {
            cout << r[0] << ' ' << r[1] << '\n';
        }
    }
    return 0;
}