#include <cstdio>

long long fac(int n){
    if (n<=1)
        return 1;
    return n*fac(n-1);
}

int main(void){
    int num;
    scanf("%d", &num);
    printf("%lld", fac(num));
}