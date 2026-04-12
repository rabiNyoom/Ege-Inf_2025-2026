#include <algorithm>
#include <cmath>
#include <iostream>
#include <vector>

using namespace std;

int F(int n) {
  vector<int> v;
  int lim = sqrt(n);
  for (int d = 1; d <= lim; d++) {
    if (n % d == 0) {
      if (d % 2 == 0)
        v.push_back(d);
      int dd = n / d;
      if (dd % 2 == 0 && dd * dd != n)
        v.push_back(dd);
    }
  }
  return v;
}

int main() {
  for (int n = 113000000; n <= 114000000; n++) {
    auto r = F(n);
    if (r.size() == 3) {
      sort(r.begin(), r.end());
      cout << n << ' ' << r[1] << '\n';
    }
  }
}