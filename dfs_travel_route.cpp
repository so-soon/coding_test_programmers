#include <string>
#include <vector>
#include <unordered_map>
#include <utility>
#include <algorithm>
using namespace std;
unordered_map<string, vector<string>> src_dst;
unordered_map<string, int> un_used;
vector<string> path;
vector<vector<string>>* t;
bool dfs(string src);
vector<string> solution(vector<vector<string>> tickets) {
    
    t = &tickets;
    
    for(int i = 0 ; i < tickets.size(); i++){
        src_dst[tickets[i][0]].push_back(tickets[i][1]);
        un_used[tickets[i][0]+tickets[i][1]] += 1; // need to check
    }
    
    path.push_back("ICN");
    dfs("ICN");
    
    
    return path;
}

bool dfs(string src){
    bool isFail = true;
    if ((t->size())+1 == path.size()) {
        return true;
    }else if(src_dst[src].empty()){
        return false;
        
        
    }else{
        if (src_dst[src].size() > 1 ) {
            sort(src_dst[src].begin(),src_dst[src].end());
            for(int j = 0 ; j < src_dst[src].size(); j++){
                
                if (un_used[src+src_dst[src][j]] != 0) {
                    path.push_back(src_dst[src][j]);
                    un_used[src+src_dst[src][j]] -= 1;
                    if(!dfs(src_dst[src][j])){
                        isFail = true;
                        path.pop_back();
                        un_used[src+src_dst[src][j]] += 1;
                    }else{
                        isFail = false;
                        break;
                    }
                }
            }
        }else{
            
            path.push_back(src_dst[src][0]);
            un_used[src+src_dst[src][0]] -= 1;
            if(!dfs(src_dst[src][0])){
                un_used[src+src_dst[src][0]] += 1;
                path.pop_back();
                isFail = true;
            }else{
                isFail = false;
            }
                
            
            
        }
        
    }
    if (isFail) {
        return false;
    }
    else return true;
}
