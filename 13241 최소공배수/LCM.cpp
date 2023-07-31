#include <cstdio>

using namespace std;


int GCD(const long long& _x, const long long& _y){
  long long temp, x = _x, y = _y, res=0;

  while(y!=0){
    temp = x%y;
    x=y;
    y=temp;
  }
  
  return x;
}


int main() {
  long long a,b,gcd,lcm;
  scanf("%lld %lld", &a, &b);
  gcd = GCD(a,b);
  lcm = a/gcd*b;
  printf("%lld", lcm);
  return 0;
}