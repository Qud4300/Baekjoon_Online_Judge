#include <iostream>
using namespace std;

int main() {
  int total;
  int n, val, count, temp;

  cin >> total;
  cin >> n;

  for (int i = 0; i < n; i++) {
    cin >> val >> count;
    temp = val * count;
    total -= temp;
  }
  if (total == 0)
    cout << "Yes";
  else
    cout << "No";
  return 0;
}
