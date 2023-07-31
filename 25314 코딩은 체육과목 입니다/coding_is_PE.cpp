#include <iostream>
#include <string>
using namespace std;

int main() {
  string l = "long ";
  int n;
  cin >> n;
  n /= 4;
  for (int i = 0; i<n-1; i++)
    cout << l;
  cout << "long int"; 
  return 0;
}
