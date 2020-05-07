#include <string>
#include <vector>
#include <set>
using namespace std;

int u_find(int x);
void u_union(int x,int y);


int root[200];
int height[200];
int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    set<int> res;
    for(int i = 0 ; i < n; i++){
        root[i] = i;
        height[i] = 0;
    }
    
    for(int i = 0 ; i < n ; i++){
        for(int j = i+1 ; j < n ; j++){
            
            if (computers[i][j] == 1) {
                u_union(i, j);
            }
        }
    }
    
    
    for(int i = 0 ; i < n; i++){
        root[i] = u_find(i);
        res.insert(root[i]);
    }
    answer = int(res.size());
    return answer;
}
int u_find(int x){
    if (root[x] == x) {
        return x;
    }else{
        return root[x] = u_find(root[x]);
    }
}
void u_union(int x,int y){
    
    x = u_find(x);
    y = u_find(y);
    
    
    if( x == y) return;
    
    if (height[x] <height[y]) {
        root[x] = y;
    }else{
        root[y] = x;
        if (height[x] == height[y]) {
            height[x]++;
        }
    }
}
