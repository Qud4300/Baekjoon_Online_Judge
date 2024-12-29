#include <iostream>

using namespace std;

// 11726 2xN tiling

int dp[1001] = {1,1};

int fibo(int a){
    if(a<2) return dp[a];
    if(not dp[a])
    {
        if (not dp[a-1])  dp[a-1] = fibo(a-1);
        dp[a] = (dp[a-1]+dp[a-2]) % 10007;
    }
    return dp[a];
}

int main(void){
    int n;
    cin >> n;
    cout << fibo(n) << endl;
    return 0;
}