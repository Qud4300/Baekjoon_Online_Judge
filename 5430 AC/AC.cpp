#include <deque>
#include <iostream>
#include <sstream>
#include <string>

using namespace std;

int main() {
  int t, n;
  string str, com, tok, empty = "";
  bool error = false, flag = false;
  deque<string> deq;

  cin >> t;
  while (t--) {
    deq.clear();
    error = false;
    flag = false;
    cin >> com;
    cin >> n;
    cin >> str;
    str.replace(0, 1, empty);
    str.replace(str.length() - 1, 1, empty);
    if (n != 0) {
      stringstream ss(str);
      while (getline(ss, tok, ',')) {
        deq.push_back(tok);
      }
    }
    for (char c : com) {
      if (c == 'R') {
        flag = !flag;
      } else if (c == 'D' && deq.size() != 0) {
        if (deq.size() != 0) {
          if (flag)
            deq.pop_back();
          else
            deq.pop_front();
        }
      } else {
        error = true;
        break;
      }
    }
    if (error) {
      cout << "error\n";
    } else {
      ostringstream oss;
      oss << '[';
      if (deq.size()){
        if (flag) {
        for (auto it = deq.rbegin(); it != deq.rend() - 1; it++) {
          oss << *it << ',';
        }
        oss << deq[0];
        } else {
          for (auto it = deq.begin(); it != deq.end() - 1; it++) {
            oss << *it << ',';
          }
          oss << deq[deq.size() - 1];
        }
      }
      oss << ']';
      cout << oss.str() << endl;
    }
  }

  return 0;
}