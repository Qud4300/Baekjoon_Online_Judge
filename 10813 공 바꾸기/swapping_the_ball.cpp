#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n, m, temp, i, j;
  vector<int> vec;

  cin >> n >> m;
  vec.resize(n);
  for (int i=0; i<n; i++)
    vec[i] = i+1;
  while(m--){
    cin >> i >> j;
    temp = vec[i-1];
    vec[i-1] = vec[j-1];
    vec[j-1] = temp;
  }
  for (int num : vec)
    cout << num << ' ';
  return 0;
}