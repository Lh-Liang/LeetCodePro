#
# @lc app=leetcode id=1206 lang=cpp
#
# [1206] Design Skiplist
#

# @lc code=start
#include <vector>
#include <cstdlib>
#include <ctime>
using namespace std;

class Node {
public:
    int val;
    vector<Node*> forward;
    Node(int val, int level) : val(val), forward(level + 1, nullptr) {}
};

class Skiplist {
private:
    Node* head;
    int maxLevel;
    float probability;
    int randomLevel() {
        int level = 0;
        while ((rand() / double(RAND_MAX)) < probability && level < maxLevel) {
            level++;
        }
        return level;
    }
public:
    Skiplist() : head(new Node(-1, 16)), maxLevel(16), probability(0.5) { srand(time(0)); } 
    bool search(int target) { 
        Node* curr = head; 
        for (int i = maxLevel; i >= 0; i--) { 
            while (curr->forward[i] && curr->forward[i]->val < target) { 
                curr = curr->forward[i]; 
            } 
        } 
        curr = curr->forward[0]; 
        return curr && curr->val == target; 
    } 
d void add(int num) { " obj->add(num);