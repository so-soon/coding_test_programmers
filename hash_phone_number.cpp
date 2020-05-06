#include <string>
#include <vector>
#include <string.h>

using namespace std;

struct Trie{
    Trie* child[10];
    bool isNum;
    
    Trie(): isNum(false) {
        memset(child,0,sizeof(child));
    }
    
    ~Trie(){
        for(int i = 0 ; i < 10 ; i++){
            if(child[i]){
                delete child[i];
            }
            
        }
    }
    
    void insert(const char* key){
        if (*(key) == '\0') {
            isNum = true;
            return;
        }else{
            int curr = *(key) - '0';
            if (child[curr] == NULL) {
                child[curr] = new Trie();
            }
            child[curr]->insert(key+1);
        }
    }
    
    bool find(const char* key){
        if (*(key) != '\0' && isNum) {
            return false;
        }else if(*(key) == '\0' && !isNum) return false;
        else if(*(key) == '\0' && isNum){
            return true;
        }else{
            int curr = *(key)-'0';
            return child[curr]->find(key+1);
        }
        
    }
    
};


bool solution(vector<string> phone_book) {
    bool answer = true;
    Trie* root = new Trie();
    
    for(int i = 0 ; i < phone_book.size() ; i++){
        root->insert(phone_book[i].c_str());
    }
    
    for(int i = 0 ; i < phone_book.size() ; i++){
        if(!(root->find(phone_book[i].c_str()))){
            answer = false;
            break;
        }
    }
    
    
    return answer;
}
