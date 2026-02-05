#
# @lc app=leetcode id=1206 lang=cpp
#
# [1206] Design Skiplist
#

# @lc code=start
#include <vector>
#include <cstdlib>
#include <ctime>

class Skiplist {
    struct Node {
        int val;
        std::vector<Node*> forward;
        Node(int v, int level) : val(v), forward(level, nullptr) {}
    };
    static constexpr int MAX_LEVEL = 16;
    static constexpr float P = 0.5;
    Node* head;
    int level;
    
    int randomLevel() {
        int lvl = 1;
        while (((double)std::rand() / RAND_MAX) < P && lvl < MAX_LEVEL) {
            lvl++;
        }
        return lvl;
    }
public:
    Skiplist() {
        std::srand(std::time(nullptr));
        head = new Node(-1, MAX_LEVEL);
        level = 1;
    }
    
    bool search(int target) {
        Node* curr = head;
        for (int i = level - 1; i >= 0; --i) {
            while (curr->forward[i] && curr->forward[i]->val < target) {
                curr = curr->forward[i];
            }
        }
        curr = curr->forward[0];
        return curr && curr->val == target;
    }
    
    void add(int num) {
        std::vector<Node*> update(MAX_LEVEL, nullptr);
        Node* curr = head;
        for (int i = level - 1; i >= 0; --i) {
            while (curr->forward[i] && curr->forward[i]->val < num) {
                curr = curr->forward[i];
            }
            update[i] = curr;
        }
        int lvl = randomLevel();
        if (lvl > level) {
            for (int i = level; i < lvl; ++i) {
                update[i] = head;
            }
            level = lvl;
        }
        Node* node = new Node(num, lvl);
        for (int i = 0; i < lvl; ++i) {
            node->forward[i] = update[i]->forward[i];
            update[i]->forward[i] = node;
        }
    }
    
    bool erase(int num) {
        std::vector<Node*> update(MAX_LEVEL, nullptr);
        Node* curr = head;
        for (int i = level - 1; i >= 0; --i) {
            while (curr->forward[i] && curr->forward[i]->val < num) {
                curr = curr->forward[i];
            }
            update[i] = curr;
        }
        curr = curr->forward[0];
        if (!curr || curr->val != num) return false;
        for (int i = 0; i < level; ++i) {
            if (update[i]->forward[i] != curr) break;
            update[i]->forward[i] = curr->forward[i];
        }
        delete curr;
        while (level > 1 && head->forward[level - 1] == nullptr) {
            --level;
        }
        return true;
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