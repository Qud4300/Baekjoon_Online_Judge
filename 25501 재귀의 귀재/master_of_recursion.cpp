#include <iostream>
#include <string>
using namespace std;

int recursion(const string& s, int l, int r, int& c){
    c+=1;
    if(l >= r) return 1;
    else if(s[l] != s[r]) return 0;
    else return recursion(s, l+1, r-1, c);
}

int isPalindrome(const string& s, int& c){
    return recursion(s, 0, s.length()-1, c);
}
int main(void){
    int t, c;
    string str;
    cin >> t;
    while(t--){
        c = 0;
        cin >> str;
        cout << isPalindrome(str, c) << ' ' << c << '\n';
    }
}