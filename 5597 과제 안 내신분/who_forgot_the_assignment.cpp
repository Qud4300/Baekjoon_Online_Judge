#include <bitset>
#include <iostream>
using namespace std;

int main() {
  int temp;
  bitset<30> bit;

  for (int i = 0; i < 28; i++) {
    cin >> temp;
    bit[temp] = 1;
  }

  for (int i = 1; i < 31; i++) {
    if (!bit[i])
      cout << i << endl;
  }
  return 0;
}