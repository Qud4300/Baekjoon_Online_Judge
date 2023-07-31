#include <iostream>
using namespace std;

int main() {
  int n, a, b, Mh = -10000, mh=10000, Mw = -10000, mw=10000;
  cin >> n;
  while(n--){
    cin >> a>> b;
    Mw = max(Mw, a);
    Mh = max(Mh, b);
    mw = min(mw, a);
    mh = min(mh, b);
  }
  cout << (Mw-mw)*(Mh-mh);
  return 0;
}