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
    int value;
    vector<Node*> forward;
    Node(int val, int level) : value(val), forward(level + 1, nullptr) {}
};

class Skiplist {
private:
    Node* head;
    int maxLevel;
    float probability;
    int randomLevel() {
        int lvl = 0;
        while ((rand() / double(RAND_MAX)) < probability && lvl < maxLevel) {
            lvl++;
        }
        return lvl;
    }
public:
    Skiplist() : maxLevel(16), probability(0.5) {
        srand(time(0));
        head = new Node(-1, maxLevel);
    }
    
bool search(int target) {
        Node* current = head;
        for (int i = maxLevel; i >= 0; i--) {
            while (current->forward[i] && current->forward[i]->value < target) {
                current = current->forward[i];
            }
        }
        current = current->forward[0];
        return current != nullptr && current->value == target;
    }
    
bool add(int num) {
g vector<Node*> update(maxLevel + 1);
g vector<Node*> update(maxLevel + 1);
d add(int num);current = head;current = head;for (int i = maxLevel; i >= 0; i--) {while (current->forward[i] && current->forward[i]->value < num) {current = current->forward[i];}update[i] = current;}int lvl = randomLevel();Node* newNode = new Node(num, lvl);for (int i = 0; i <= lvl; i++) {newNode->forward[i] = update[i]->forward[i];update[i]->forward[i] = newNode;}return true;
bool erase(int num) {
erase(num);bool erase(num);erase(num);bool erase(num);erase(num);erase(num);
erase(num);}