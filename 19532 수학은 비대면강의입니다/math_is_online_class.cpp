#include <iostream>
using namespace std;

int main() {
  int a, b, c, d, e, f, x, y;
  cin >> a >> b >> c >> d >> e >> f;
  if (a==0){
    y = c/b;
    x = (f-e*y)/d;
  } else if (b==0){
    x = c/a;
    y = (f-d*x)/e;
  } else{
    x = (c * e - b * f) / (a * e - b * d);
    y = (c - a * x) / b;
  }
  cout << x << ' ' << y;
  return 0;
}