#include <iostream>
#include <set>
#include <string>

using namespace std;

int main() {
  string str;
  string tok;
  set<string> s;
  int len;
  cin >> str;

  for (int l = 1; l < str.length() + 1; l++){
    for (int i =0; i < str.length()+1-l; i++){
      tok = str.substr(i, l);
      s.insert(tok);
    }
  }
  printf("%d", (int)s.size());
  return 0;
}