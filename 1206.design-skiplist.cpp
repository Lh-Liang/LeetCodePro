#
# @lc app=leetcode id=1206 lang=cpp
#
# [1206] Design Skiplist
#

# @lc code=start
#include <vector>
#include <cstdlib>

using namespace std;

class Skiplist {
    struct Node {
        int val;
        vector<Node*> next;
        Node(int v, int level) : val(v), next(level, nullptr) {}
    };

    Node* head;
    static const int MAX_LEVEL = 16;

public:
    Skiplist() {
        head = new Node(-1, MAX_LEVEL);
    }
    
    ~Skiplist() {
        Node* curr = head;
        while (curr) {
            Node* temp = curr;
            curr = curr->next[0];
            delete temp;
        }
    }

    bool search(int target) {
        Node* curr = head;
        for (int i = MAX_LEVEL - 1; i >= 0; i--) {
            while (curr->next[i] && curr->next[i]->val < target) {
                curr = curr->next[i];
            }
        }
        curr = curr->next[0];
        return curr != nullptr && curr->val == target;
    }

    void add(int num) {
        vector<Node*> update(MAX_LEVEL, head);
        Node* curr = head;
        for (int i = MAX_LEVEL - 1; i >= 0; i--) {
            while (curr->next[i] && curr->next[i]->val < num) {
                curr = curr->next[i];
            }
            update[i] = curr;
        }

        int lvl = randomLevel();
        Node* newNode = new Node(num, lvl);
        for (int i = 0; i < lvl; i++) {
            newNode->next[i] = update[i]->next[i];
            update[i]->next[i] = newNode;
        }
    }

    bool erase(int num) {
        vector<Node*> update(MAX_LEVEL, head);
        Node* curr = head;
        for (int i = MAX_LEVEL - 1; i >= 0; i--) {
            while (curr->next[i] && curr->next[i]->val < num) {
                curr = curr->next[i];
            }
            update[i] = curr;
        }

        curr = curr->next[0];
        if (!curr || curr->val != num) return false;

        for (int i = 0; i < MAX_LEVEL; i++) {
            if (update[i]->next[i] != curr) break;
            update[i]->next[i] = curr->next[i];
        }
        delete curr;
        return true;
    }

private:
    int randomLevel() {
        int lvl = 1;
        while (lvl < MAX_LEVEL && (rand() & 1)) {
            lvl++;
        }
        return lvl;
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