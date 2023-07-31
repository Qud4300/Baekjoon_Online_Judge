#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> vec;
  int n, m, i, j, k;

  cin >> n >> m;
  vec.assign(n, 0);
  while (m--) {
    cin >> i >> j >> k;
    fill(&vec[i - 1], &vec[j], k);
  }

  for (int num : vec) {
    cout << num << ' ';
  }
  return 0;
}