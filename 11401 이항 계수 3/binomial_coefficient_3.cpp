// BOJ 11401 이항 계수 3 - 페르마의 소정리
#include <vector>
#include <iostream>

using namespace std;
const static int p = 1000000007;

long long power(long long A, long long B){
    long long res = 1;
    while(B) {
        if (B & 1) {
            // whatever 'B' is, always becomes 1 and then go 0.
            // so no need to worry 'A' being missed out from multiplication.
            res = (res * A) % p;
        }
        A = (A * A) % p;
        B >>= 1;
    }
    return res;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    long long n,k,i,N,NK;
    cin >> n >> k;

    if (k > n/2) k = n-k;
    
    vector<long long> fac = {1,1};
    for(i = 2; i<n+1; i++){
        fac.push_back(fac[i-1] * i % p);
    }
    N = fac[n];
    NK = fac[n-k]*fac[k]%p;
    NK = power(NK, p-2) % p;
    cout << (N*NK)%p;
    return 0;
}
