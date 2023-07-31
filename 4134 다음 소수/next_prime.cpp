#include <cstdio>
#include <cmath>

using namespace std;

bool isPrime(const long long& _a){
  if(_a==1 || _a==0)
    return false;
  long long a = _a;
  for (int i = 2; i<(int)sqrt(a)+1; i++){
    if(a%i==0)
      return false;
  }
  return true;
} 

int main() {
  long long n; 
  int t;
  scanf("%u", &t);
  while (t--){
    scanf("%lld", &n);
    while(!isPrime(n))
      n++;
    printf("%lld\n", n);
  }
  return 0;
}