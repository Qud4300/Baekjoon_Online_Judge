#include <cstdio>
#include <set>
using namespace std;

int main() {
  int n, t;
  set<int> s;
  scanf("%d", &n);
  while (n--) {
    scanf(" %d", &t);
    s.insert(t);
  }
  scanf("%d", &n);
  while (n--) {
    scanf(" %d", &t);
    if (s.find(t) != s.end())
      printf("1 ");
    else
      printf("0 ");
  }
  return 0;
}