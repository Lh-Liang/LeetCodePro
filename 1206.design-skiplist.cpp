#
# @lc app=leetcode id=1206 lang=cpp
#
# [1206] Design Skiplist
#

# @lc code=start
#include <vector>
#include <random>
#include <algorithm>

using namespace std;

struct Node {
    int val;
    vector<Node*> forward;
    
    Node(int v, int level) : val(v), forward(level, nullptr) {}
};

class Skiplist {
private:
    Node* head;
    int maxLevel;
    const int MAX_LEVEL = 32;
    const float P = 0.5;
    
    // Random level generator
    int randomLevel() {
        int lvl = 1;
        while ((float)rand() / RAND_MAX < P && lvl < MAX_LEVEL) {
            lvl++;
        }
        return lvl;
    }

public:
    Skiplist() {
        head = new Node(-1, MAX_LEVEL);
        maxLevel = 0; // Current highest level containing actual data
        srand(time(0));
    }
    
    bool search(int target) {
        Node* curr = head;
        // Start from the highest level and go down
        for (int i = maxLevel - 1; i >= 0; i--) {
            while (curr->forward[i] && curr->forward[i]->val < target) {
                curr = curr->forward[i];
            }
        }
        // Move to the next node at level 0
        curr = curr->forward[0];
        return curr && curr->val == target;
    }
    
    void add(int num) {
        vector<Node*> update(MAX_LEVEL, nullptr);
        Node* curr = head;
        
        // Find the position to insert at all levels
        for (int i = maxLevel - 1; i >= 0; i--) {
            while (curr->forward[i] && curr->forward[i]->val < num) {
                curr = curr->forward[i];
            }
            update[i] = curr;
        }
        
        int lvl = randomLevel();
        
        // If the new level is higher than current maxLevel, update the head's forward pointers
        if (lvl > maxLevel) {
            for (int i = maxLevel; i < lvl; i++) {
                update[i] = head;
            }
            maxLevel = lvl;
        }
        
        // Create new node and insert links
        Node* newNode = new Node(num, lvl);
        for (int i = 0; i < lvl; i++) {
            newNode->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = newNode;
        }
    }
    
    bool erase(int num) {
        vector<Node*> update(MAX_LEVEL, nullptr);
        Node* curr = head;
        
        // Find the predecessor nodes at all levels
        for (int i = maxLevel - 1; i >= 0; i--) {
            while (curr->forward[i] && curr->forward[i]->val < num) {
                curr = curr->forward[i];
            }
            update[i] = curr;
        }
        
        curr = curr->forward[0];
        
        // If target found
        if (curr && curr->val == num) {
            for (int i = 0; i < maxLevel; i++) {
                if (update[i]->forward[i] != curr) {
                    break;
                }
                update[i]->forward[i] = curr->forward[i];
            }
            
            // Remove empty levels
            while (maxLevel > 0 && head->forward[maxLevel - 1] == nullptr) {
                maxLevel--;
            }
            
            delete curr;
            return true;
        }
        
        return false;
    }
};

/**
 * Your Skiplist object will be instantiated and called as such:
 * Skiplist* obj = new Skiplist();
 * bool param_1 = obj->search(target);
 * obj->add(num);
 * bool param_3 = obj->erase(num);
 */
# @lc code=end