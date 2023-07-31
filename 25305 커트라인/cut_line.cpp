#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
  int n, k, t;
  vector<int> vec;

  cin >> n >> k;
  vec.resize(n);
  while(n--){
    cin >> t;
    vec.push_back(t);
  }
  sort(vec.rbegin(), vec.rend());
  cout << vec[k-1];
  return 0;
}