#
# @lc app=leetcode id=1206 lang=cpp
#
# [1206] Design Skiplist
#
# @lc code=start
#include <vector>
#include <limits.h>
#include <cstdlib> // For rand()
#include <ctime>   // For time()
using namespace std;

class Node {
public:
    int val;
    vector<Node*> forward;
    Node(int val, int level) : val(val), forward(level, nullptr) {}
};

class Skiplist {
private:
    Node* head;
    int maxLevel;
    float probability; // Probability factor for level generation
    int currentLevel;

public:
    Skiplist() : maxLevel(16), probability(0.5), currentLevel(0) {
        head = new Node(INT_MIN, maxLevel);
        srand(time(NULL)); // Seed for random level generation
    }

    int randomLevel() {
        int lvl = 1;
        while (lvl < maxLevel && ((float)rand() / RAND_MAX) < probability) {
            lvl++;
        }
        return lvl;
    }

    bool search(int target) {
        Node* curr = head;
        for (int i = currentLevel; i >= 0; --i) {
            while (curr->forward[i] && curr->forward[i]->val < target) {
                curr = curr->forward[i];
            }
        }
        curr = curr->forward[0];
        return curr && curr->val == target;
    }

    void add(int num) {
        vector<Node*> update(maxLevel);
        Node* curr = head;
        for (int i = currentLevel; i >= 0; --i) {		while(curr->forward[i] && curr->forward[i]->val<num){curr=curr->forward[i];}update[i]=curr;}int lvl=randomLevel();if(lvl>currentLevel){for(int=i=currentLe+1;i<lvl;++i){update[i]=head;}currentLe=lvl-1;}Node* newNode=newNode(num,lvl);for(int=i=0;i<lvl;++i){newNode-forwar[i]=update[i]-forw-update[i]-for=i=newNod-;}}
bool erase(int num){vector<Node*>update(maxLe);Node*c=head;for(int=i=currentLe;l>=0;i--){whil(c-forw&&c-forwd-<num)c=c-forwd[update[=c;}c=c-forwd[if(!c||c-val!=num)return false;for(int=i=<=currentLe;++){if(update[>forw!=c)brea}update[>forw]=c-forwd[while(currentLe>0&&head-forw[current]==nullptr)--currentLedelete crurn true;