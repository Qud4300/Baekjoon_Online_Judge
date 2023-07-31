#include <cstdio>
#include <map>
#include <numeric>
#include <set>
#include <vector>
using namespace std;

int main() {
  int n, t;

  vector<int> vec;
  map<int, int> dict;
  set<int> s;
  scanf("%d", &n);
  vec.resize(n);
  while (n--) {
    scanf(" %d", &t);
    vec.push_back(t);
    s.insert(t);
  }
  t = 0;
  for (auto iter = s.begin(); iter != s.end(); iter++, t++) {
    dict.insert({*iter, t});
  }
  for (int i : vec) {
    auto iter = dict.find(i);
    if (iter != dict.end()) {
      printf("%d ", iter->second);
    }
  }
  return 0;
}