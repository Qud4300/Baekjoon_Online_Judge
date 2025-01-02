#include <iostream>
#include <vector>
#include <tuple>
#include <queue>

using namespace std;
typedef tuple<int,int,int> coord;
typedef vector<vector<int>> vector2D;

bool Is_Rectangle(vector2D &arr, coord c){
    int row = get<0>(c), col = get<1>(c), size = get<2>(c);
    int color = arr[row][col];

    for(int i = 0; i < size; i++){
        for(int j = 0; j < size; j++){
            if(arr[row + i][col + j] != color){
                return false;
            }
        }
    }
    return true;
}

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int N, white = 0 , blue = 0;
    int row,col,size;
    cin >> N;
    vector2D rect(N, vector<int>(N));
    queue<coord> Q;
    for(int i =0; i<N; i++){
        for(int j = 0; j<N; j++){
            cin >> rect[i][j];
        }
    }
    Q.push(coord(0,0,N));
    while(!Q.empty()){
        coord elem = Q.front();
        Q.pop();
        tie(row,col,size) = elem;
        if(!Is_Rectangle(rect, elem)){
            int HalfSize = size/2;
            Q.push(coord(row, col, HalfSize));
            Q.push(coord(row+HalfSize, col, HalfSize));
            Q.push(coord(row, col+HalfSize, HalfSize));
            Q.push(coord(row+HalfSize, col+HalfSize, HalfSize));
        }
        else{
            int color = rect[row][col];
            if(color){
                blue += 1;
            }
            else{
                white += 1;
            }
        }
    }
    cout << white << '\n' << blue;
}