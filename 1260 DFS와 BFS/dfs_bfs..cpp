// BOJ 1260 BFS와 DFS
#include <stdio.h>
#include <vector>
#include <array>
#include <queue>
#include <bitset>
using namespace std;

bitset<1001> visited;
array<vector<int>,1001> edges;

/* DFS written in recursive call style. */
void DFS(int v){
    printf("%d ",v);
    visited.set(v);
    auto a = edges[v];
    for(auto dest : a) {
        if (!visited[dest])
            DFS(dest);
    }
}

/* BFS written in for-loop style. */
void BFS(int v){
    queue<int> temp;
    int cur;
    temp.push(v);
    visited.set(v);
    printf("%d ",v);
    while (!temp.empty()) {
        cur = temp.front();
        for (int dest: edges[cur]) {
            if(!visited[dest]){
                printf("%d ",dest);
                visited[dest]=true;
                temp.push(dest);
            }
        }
        temp.pop();
    }
}



int main() {
    //n: number of vertices. m: number of edges. s: index of starting vertex.
    int n, m, s, i; // you know, 'i' for iterator.
    int _x=0,_y=0; //var for input receiving use.
    visited.reset();

    scanf("%d %d %d", &n, &m, &s);
    for(i = m; i!=0; i--) { // receive m-edge info.
        scanf("%d %d", &_x, &_y);
        edges[_x].push_back(_y);
        edges[_y].push_back(_x);
    }
    for(vector<int> &edge : edges){ // sort adjacency list.
        sort(edge.begin(), edge.end());
    }
    DFS(s);
    printf("\n");
    visited.reset();
    BFS(s);
    return 0;
}
