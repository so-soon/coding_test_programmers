#include <string>
#include <vector>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds) {
    vector<int> answer;
    vector<int> s;
    int curr;
    for(int i = 0 ; i < progresses.size(); i++){
        curr = int((100-progresses[i])/speeds[i]);
        if ((100-progresses[i]) % speeds[i] != 0) {
            curr++;
        }
        
        if (!s.empty()) {
            if (curr <= s.front()) {
                s.push_back(curr);
            }else{
                answer.push_back(int(s.size()));
                s.clear();
                s.push_back(curr);
            }
        }else{
            s.push_back(curr);
        }
        
        
    }
    
    if (!s.empty()) {
        answer.push_back(int(s.size()));
        s.clear();
    }
    
    return answer;
}
