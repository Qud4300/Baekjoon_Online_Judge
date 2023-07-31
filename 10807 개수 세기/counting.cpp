#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main() {
  int n, temp, v;
  vector<int> vec;

  cin >> n;
  for (int i = 0; i < n; i++) {
    cin >> temp;
    vec.push_back(temp);
  }
  cin >> v;
  cout << count(vec.begin(), vec.end(), v);
  return 0;
}
