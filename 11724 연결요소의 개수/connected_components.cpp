#include <iostream>
#include <vector>
// #include <algorithm>
// #include <numeric>
// #include <math.h>
// #include <string>
// #include <map>
// #include <tuple>
#include <queue>
// #include <set>

using namespace std;
typedef vector<vector<int>> Vector2D;

// BOJ 11724 연결 요소의 개수
/*
풀이 접근.

**시간초과!!!
dfs말고 bfs로 하자. 

*/
void dfs(Vector2D& G, vector<int>& P, vector<bool>& V, int a){
    V[a] = true;
    for(int b: G[a]){
        P[b] = a;
        dfs(G,P, V, b);
    }
    return;
}

void bfs(Vector2D& G, vector<int>& P, vector<bool>& V, int a){
    V[a] = true;
    queue<int> Q = queue<int>();
    Q.push(a);
    while(!Q.empty()){
        int cur = Q.front(); Q.pop();
        for(int b: G[cur]){
            P[b] = a;
            // if b is not visited, add to seach queue.
            if(!V[b]){
                Q.push(b);
                V[b] = true; // mark b as visited, so that another accessing from other edge after this would not cause double-visiting.
            }
        }
    }
    return;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int n, m, a, b, small, big, res=0;
    cin >> n >> m;
    Vector2D edges(n+1); 
    vector<int> parent(n+1);
    for(int i = 1; i<n+1; i++){
        parent[i] = i;
    }
    vector<bool> visited(n+1, false);
    for(int _ = 0; _<m; _++){
        cin >> a >> b;
        edges[a].push_back(b);
        edges[b].push_back(a);
    }

    for(int i = 1; i<n+1; i++){
        if(!visited[i]){
            res += 1;
            bfs(edges, parent, visited, i);
        }
    }
    cout << res;
}