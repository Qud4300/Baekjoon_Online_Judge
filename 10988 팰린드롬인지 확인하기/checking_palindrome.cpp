#include <iostream>
#include <string>
using namespace std;

int main() {
  string s;
  int m;
  cin >> s;
  m = s.length()/2;
  for (int i = 0; i<m; i++){
    if (s[i] != s[s.length()-1-i]){
      cout << 0;
      return 0;
    }
  }
  cout << 1;
  return 0;
}