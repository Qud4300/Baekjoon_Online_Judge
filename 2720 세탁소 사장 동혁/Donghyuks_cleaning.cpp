#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  int t, c, q, d, n, p;
  cin >> t;
  while (t--) {
    cin >> c;
    q = c/25;
    c %= 25;
    d = c/10;
    c %= 10;
    n = c/5;
    c %= 5;
    p = c;
    cout << q << ' ' << d << ' ' << n << ' ' << p << endl;
  }
  return 0;
}