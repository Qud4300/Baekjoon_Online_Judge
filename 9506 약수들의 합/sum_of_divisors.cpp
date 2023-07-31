#include <iostream>
#include <numeric>
#include <vector>
using namespace std;

void getMeasure(vector<int> &v, const int &num) {
  for (int i = 1; i < num; i++) {
    if (num % i == 0)
      v.push_back(i);
  }
}

int main() {
  vector<int> vec;
  int n;
  while (1) {
    vec.clear();
    cin >> n;
    if (n == -1)
      break;
    getMeasure(vec, n);
    if (accumulate(vec.begin(), vec.end(), 0) == n) {
      cout << n << " = ";
      for (int i = 0; i < vec.size() - 1; i++) {
        cout << vec[i] << " + ";
      }
      cout << vec[vec.size() - 1] << endl;
    } else {
      cout << n << " is NOT perfect." << endl;
    }
  }
  return 0;
}