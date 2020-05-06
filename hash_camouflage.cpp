#include <string>
#include <vector>
#include <unordered_map>
#include <math.h>

using namespace std;

unordered_map<string, int> clothes_num;

int solution(vector<vector<string>> clothes) {
    int answer = 1;
    
    for(int i = 0 ; i < clothes.size(); i++){
        clothes_num[clothes[i][1]]++;
    }
    
    for(unordered_map<string, int>::iterator iter = clothes_num.begin(); iter != clothes_num.end(); ++iter){
        answer *= ((iter->second)+1);
    }
    return answer-1;
}
