#include <string>
#include <vector>

using namespace std;

vector<int> solution(int brown, int red) {
    vector<int> answer;
    
    for(int i = red ; i >= (red/i) ; i--){
        if (red%i != 0) {
            continue;
        }
        if (((2*i)+(2*(red/i))+4) == brown) {
            answer.push_back(i+2);
            answer.push_back((red/i)+2);
            break;
        }
        
    }
    
    return answer;
}
