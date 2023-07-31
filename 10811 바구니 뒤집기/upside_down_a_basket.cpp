#include <vector>
#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
  vector<int> vec;
  int n, m, i, j;
  cin >> n >> m;
  vec.resize(n+1);
  iota(vec.begin()+1, vec.end(), 1);
  while (m--){
    cin >> i >> j;
    reverse(&vec[i], &vec[j]+1);
  }
  for (int i=1; i<n+1; i++)
    cout << vec[i] << ' ';
  return 0;
}