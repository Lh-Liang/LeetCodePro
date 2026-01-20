#
# @lc app=leetcode id=1206 lang=cpp
#
# [1206] Design Skiplist
#

# @lc code=start
#include <cstdlib>

class Skiplist {
private:
    static const int MAX_LEVEL = 16;
    
    struct Node {
        int val;
        Node* next[MAX_LEVEL];
        Node(int v) : val(v) {
            for (int i = 0; i < MAX_LEVEL; ++i) {
                next[i] = nullptr;
            }
        }
    };

    Node* head;

public:
    Skiplist() {
        head = new Node(-1);
    }
    
    ~Skiplist() {
        Node* curr = head;
        while (curr) {
            Node* temp = curr->next[0];
            delete curr;
            curr = temp;
        }
    }
    
    bool search(int target) {
        Node* curr = head;
        for (int i = MAX_LEVEL - 1; i >= 0; --i) {
            while (curr->next[i] && curr->next[i]->val < target) {
                curr = curr->next[i];
            }
        }
        curr = curr->next[0];
        return curr && curr->val == target;
    }
    
    void add(int num) {
        Node* update[MAX_LEVEL];
        Node* curr = head;
        for (int i = MAX_LEVEL - 1; i >= 0; --i) {
            while (curr->next[i] && curr->next[i]->val < num) {
                curr = curr->next[i];
            }
            update[i] = curr;
        }

        int lv = 1;
        while (lv < MAX_LEVEL && (rand() % 2 == 0)) {
            lv++;
        }

        Node* newNode = new Node(num);
        for (int i = 0; i < lv; ++i) {
            newNode->next[i] = update[i]->next[i];
            update[i]->next[i] = newNode;
        }
    }
    
    bool erase(int num) {
        Node* update[MAX_LEVEL];
        Node* curr = head;
        for (int i = MAX_LEVEL - 1; i >= 0; --i) {
            while (curr->next[i] && curr->next[i]->val < num) {
                curr = curr->next[i];
            }
            update[i] = curr;
        }

        Node* target = curr->next[0];
        if (!target || target->val != num) {
            return false;
        }

        for (int i = 0; i < MAX_LEVEL; ++i) {
            if (update[i]->next[i] != target) {
                break;
            }
            update[i]->next[i] = target->next[i];
        }
        delete target;
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