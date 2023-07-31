#include <cstdio>
#include <set>
#include <cstring>
#include <string>
using namespace std;
char enter[6] = "enter";
char leave[6] = "leave";

int main() {
  int n;
  char name[6], stat[6];
  string t;
  set<string> s;
  scanf("%d", &n);
  while (n--) {
    scanf("%s", name);
    scanf("%s", stat);
    if (strcmp(stat, enter)==0){
      s.insert(name);
    }
    else if (strcmp(stat, leave)==0){
      s.erase(name);
    }
  }

  for (set<string>::reverse_iterator e = s.rbegin(); e != s.rend(); e++){
    printf("%s\n", e->c_str());
  }
  
  return 0;
}