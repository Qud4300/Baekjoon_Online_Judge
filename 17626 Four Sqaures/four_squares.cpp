#include <iostream>
#include <vector>
// #include <algorithm>
// #include <numeric>
#include <math.h>
// #include <string>
// #include <map>

using namespace std;

// BOJ 17626 Four Squares
/*
풀이 접근.

DP[n] = PossibleMax + DP[n-PossibleMax] 이다.(이 때, PossibleMax는 n 이하의 가능한 큰 제곱수).
단, DP[n-PossibleMax]의 값이 3 이하여야 한다.
가능한 큰 제곱수 부터 시작하여 점점 줄여가면서 n-PossibleMax의 DP값이 3 이하인 매칭을 찾으면 된다.

이 때, PossibleMax의 탐색범위는 floor(sqrt(n)) 이하 n-PossibleMax 까지로 한다.
*/

int BiggestRootUnder(int a){
    if(a < 2) return 1;

    int b = trunc(sqrt(a));
    return b;
}

void presolve(vector<int>& dp, vector<bool>& visited, int n){
    int RANGE = int(sqrt(n))+1;
    for(int i=1; i<RANGE; i++){
        int I = i*i;
        for(int k = 1; k<5; k++){
            if(I*k > n) break;
            dp[I*k] = k;
            visited[I*k] = true;
        }
    }
}

int solve(vector<int>& dp, vector<bool>& visited, int a){
    if(a==0 || a==1) return 1;
    if(dp[a] == 1) return 1;

    int res = dp[a];
    int PossibleMaxRoot = BiggestRootUnder(a);
    for(int i = PossibleMaxRoot; i*i > a-PossibleMaxRoot*PossibleMaxRoot-1 ; i--){
        int temp = a - i*i;
        if(!visited[temp]){
            dp[temp] = solve(dp, visited, temp);
        }
        if(dp[temp]+1 < res){
            res = dp[temp] + 1;
        }
    }
    visited[a] = true;
    dp[a] = res;
    return res;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    vector<int> DP;
    vector<bool> Visited;
    int N;

    cin >> N;
    int sqrtn = trunc(sqrt(N));
    if(sqrtn*sqrtn==N){
        cout << 1;
        return 0;
    }

    DP.resize(N+1, 99);
    Visited.resize(N+1, false);
    DP[0]=0;
    presolve(DP, Visited, N);
    cout << solve(DP, Visited, N) << '\n';
}