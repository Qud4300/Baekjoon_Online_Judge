// BOJ 11689 GCD(n,k)=1
#include <stdio.h>
#include <vector>
#include <array>
#include <cmath>

using namespace std;
using arrLL = array<long long,2>;
int main(){
    vector<arrLL> factors;

    long long count, n, phi = 1;
    scanf("%lld", &n);
    for (long long i = 2; i<(int)sqrt(n)+1; i++){
        count = 0;
        while(n%i==0){
            n/=i;
            count++;
        }
        if (count) phi *= (i - 1) * (long long)pow(i, count - 1);
        if (n==1) break;
    }
    if (n!=1)
        phi *= (n - 1);
    printf("%lld", phi);
    return 0;
}