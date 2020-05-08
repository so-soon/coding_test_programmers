#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> heights) {
    vector<int> answer;
    for(int i = 0 ; i < heights.size(); i++){
        answer.push_back(0);
    }
    
    for(int i = 1 ; i < heights.size(); i++){
        int com = i;
        while(true){
            if (heights[com-1] > heights[i]) {
                answer[i] = com;
                break;
            }else{
                com = answer[com-1];
                if (com == 0) {
                    break;
                }
            }
            
        }
        
    }
    
    return answer;
}
