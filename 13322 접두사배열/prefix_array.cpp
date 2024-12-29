#include <iostream>
#include <string>

using namespace std;

// BOJ 13322 접두사 배열
/*
풀이 접근.

주어지는 문자열의 모든 가능한 접두사를 구한 뒤, 각 접두사들이 사전순 정렬되었을 때의 인덱스를 순서대로 출력하라.
-인덱스: 어떤 접두사가 본래 문자열에서 존재하는 위치 (ex. Cat의 접두사 Ca는 1이고, C는 0, Cat는 2이다.)

풀이: 어떤 문자열에서 접두사들을 정렬한다고 사전순서는... 변하나?
bad -> b, ba, bad
art -> a, ar, art
안변함!

그냥 문자열 길이만큼 i 증가시키면서 출력하면 된다.
*/
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    string s;

    cin >> s;

    for(int i = 0; i < s.size(); i++){
        cout << i << '\n';
    }
}