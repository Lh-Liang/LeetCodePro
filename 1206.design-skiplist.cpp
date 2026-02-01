#
# @lc app=leetcode id=1206 lang=cpp
#
# [1206] Design Skiplist
#

# @lc code=start
#include <vector>
#include <cstdlib>

class Skiplist {
    struct Node {
        int val;
        std::vector<Node*> next;
        Node(int v, int l) : val(v), next(l, nullptr) {}
    };

    Node* head;
    int maxLevel;

public:
    Skiplist() {
        maxLevel = 16;
        head = new Node(-1, maxLevel);
    }

    ~Skiplist() {
        Node* curr = head;
        while (curr) {
            Node* next = curr->next[0];
            delete curr;
            curr = next;
        }
    }

    bool search(int target) {
        Node* curr = head;
        for (int i = maxLevel - 1; i >= 0; i--) {
            while (curr->next[i] && curr->next[i]->val < target) {
                curr = curr->next[i];
            }
        }
        curr = curr->next[0];
        return curr != nullptr && curr->val == target;
    }

    void add(int num) {
        std::vector<Node*> update(maxLevel);
        Node* curr = head;
        for (int i = maxLevel - 1; i >= 0; i--) {
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
        std::vector<Node*> update(maxLevel);
        Node* curr = head;
        for (int i = maxLevel - 1; i >= 0; i--) {
            while (curr->next[i] && curr->next[i]->val < num) {
                curr = curr->next[i];
            }
            update[i] = curr;
        }

        curr = curr->next[0];
        if (!curr || curr->val != num) {
            return false;
        }

        for (int i = 0; i < (int)curr->next.size(); i++) {
            update[i]->next[i] = curr->next[i];
        }
        delete curr;
        return true;
    }

private:
    int randomLevel() {
        int lvl = 1;
        while (lvl < maxLevel && (rand() & 1)) {
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