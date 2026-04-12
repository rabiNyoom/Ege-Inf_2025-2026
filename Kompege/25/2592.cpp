#include <algorithm>
#include <cmath>
#include <iostream>

using namespace std;

int F(int n) {
  int c = 0;
  int m = 0;
  int lim = sqrt(n);
  for (int d = 1; d <= lim; d++) {
    if (n % d == 0) {
      if (d % 2 == 1) {
        c++;
        m = max(m, d);
      }
      int dd = n / d;
      if (dd % 2 == 1 && dd * dd != n) {
        c++;
        m = max(m, d);
      }
    }
  }
  if (c == 5)
    return m;
  return 0;
}

int main() {
  for (int n = 55000000; n <= 60000000; n++) {
    int r = F(n);
    if (r) {
      cout << n << ' ' << r << '\n';
    }
  }
}