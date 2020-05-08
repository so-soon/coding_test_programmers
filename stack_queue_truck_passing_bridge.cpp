#include <string>
#include <vector>
#include <queue>
#include <utility>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights) {
    int time = 1;
    int loaded_weight = 0;
    int load_target_num = 0;
    
    queue<pair<int,int> > bridge;
    
    
    
    do{
        if (!bridge.empty()) {
            if (bridge.front().second == time) {
                loaded_weight -= bridge.front().first;
                bridge.pop();
            }
        }
        
        if ((loaded_weight < weight) && ((weight-loaded_weight) >= truck_weights[load_target_num]) && load_target_num < truck_weights.size()) { // load available
            
            bridge.push(pair<int, int>( truck_weights[load_target_num] , time+bridge_length ));
            loaded_weight += truck_weights[load_target_num];
            load_target_num++;
            time++;
        }else if(!bridge.empty()){ //load unavailable
            time = bridge.front().second;
        }
        
    }while((load_target_num < truck_weights.size()) || !bridge.empty());
    
    return time;
}
