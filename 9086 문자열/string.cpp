#include <iostream>
#include <string>
using namespace std;

int main() {
  string s;
  int i;
  cin >> i;
  while (i--){
    cin >> s;
    cout << s[0] << s[s.length()-1] << endl;
  }
  return 0;
}