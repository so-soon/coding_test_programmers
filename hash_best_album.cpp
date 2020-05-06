#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <utility>

using namespace std;
map<string,int> play_n;
vector<pair<string,int>> v;
map<string,vector<int>> g_n;
vector<int> p;
bool cmp1(pair<string, int> x, pair<string, int> y);
bool cmp2(int x,int y);
vector<int> solution(vector<string> genres, vector<int> plays) {
    vector<int> answer;
    p = plays;
    for(int i = 0 ; i < genres.size(); i++){
        play_n[genres[i]] += plays[i];
        g_n[genres[i]].push_back(i);
    }
    
    for(auto iter = play_n.begin(); iter != play_n.end(); ++iter){
        v.push_back(pair<string, int>(iter->first,iter->second));
    }
    
    sort(v.begin(), v.end(), cmp1);
    
    for(int i = 0; i < v.size(); i++){
        sort(g_n[v[i].first].begin(), g_n[v[i].first].end(), cmp2);
        
        for(int j = 0 ; j < 2; j++){
            answer.push_back(g_n[v[i].first][j]);
            if (g_n[v[i].first].size() == 1) {
                break;
            }
        }
        
        
    }
    
    
    return answer;
}

bool cmp1(pair<string, int> x, pair<string, int> y){
    return x.second > y.second;
}
bool cmp2(int x,int y){
    if (p[x] == p[y]) {
        return x < y;
    }else{
        return p[x] > p[y];
    }
    
}
