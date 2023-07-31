#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main() {
  vector<string> str(5);
  int max_len = 0;
  for (int i = 0; i < 5; i++) {
    cin >> str[i];
    max_len = max(max_len, int(str[i].length()));
  }
  for (int i = 0; i < max_len; i++) {
    for (int j = 0; j < 5; j++) {
      if (str[j].length() > i)
        cout << str[j][i];
    }
  }
  return 0;
}