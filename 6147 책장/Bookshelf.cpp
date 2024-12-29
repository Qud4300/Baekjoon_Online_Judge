#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

// BOJ 6147 Bookshelf.
/*
풀이 접근.

N마리의 소, 각 소의 키 H_i, 모든 소의 키의 합 S, 책장의 높이 B.
입력: N, B
입력: N개 라인에 각 소의 신장 H_i.

1 <= B <= S < 20억+7 일때, B 이상의 높이를 만족시킬 수 있는 최소한의 소 탑의 구성요소 개수를 출력.
(소는 스택 형태로 탑쌓을 수 있다.)

즉, 입력받은 키 중 가장 큰 a개 만큼의 합이 B 이상일 때, a를 구하는 것.

*/
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    size_t N, B, temp;
    cin >> N >> B;

    vector<int> numbers(N);
    for (size_t i = 0; i < N; ++i) {
        cin >> numbers[i];
    }

    sort(numbers.begin(), numbers.end(), greater<>());

    temp = 0;
    for(int i=0; i<N; i++){
        temp += numbers[i];
        if(temp >= B){
            cout << i+1;
            return 0;
        }
    }
}