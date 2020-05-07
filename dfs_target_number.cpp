#include <string>
#include <vector>

using namespace std;

void dfs(int depth,int tot);

vector<int> nums;
int t,co;
int solution(vector<int> numbers, int target) {
    int answer = 0;
    nums = numbers;
    t = target;
    co = 0;
    dfs(0, 0);
    answer = co;
    return answer;
}
void dfs(int depth,int tot){
    if (depth == int(nums.size())) {
        if (tot == t) {
            co++;
        }
        return;
    }
    else{
        dfs(depth+1, tot+nums[depth]);
        
        dfs(depth+1, tot-nums[depth]);
        
    }
    
}
