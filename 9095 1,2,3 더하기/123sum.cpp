#include <iostream>
// #include <algorithm>
#include <numeric>
// #include <math.h>
#include <vector>
// #include <string>
// #include <map>

using namespace std;

// BOJ 9095
/*
풀이 접근.

규칙이 있는 수열.
n > 3 인 n에 대하여, n을 (1,2,3)의 합으로 나타내는 경우의 수를 F(n)이라 할 때,
F(n)=F(n-1)+F(n-2)+F(n-3) 이다.

*/

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int T;
    cin >> T;
    vector<int> arr(T);
    for(int i=0; i<T; i++){
        cin >> arr[i];
    }
    auto M = *max(arr.begin(), arr.end());
    vector<int> DP = {0, 1, 2, 4};
    for(int i=4; i<12; i++){
        DP.push_back(accumulate(DP.end()-3, DP.end(), 0));
    }
    for(int i=0; i<T; i++){
        cout << DP[arr[i]] << '\n';
    }
}