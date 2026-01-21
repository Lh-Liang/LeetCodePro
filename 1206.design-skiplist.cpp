#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=1206 lang=cpp
 *
 * [1206] Design Skiplist
 */

// @lc code=start
class Skiplist {
    static constexpr int MAX_LEVEL = 16;

    struct Node {
        int val;
        vector<Node*> next;
        Node(int v, int level) : val(v), next(level, nullptr) {}
    };

    Node* head;
    int curLevel; // current maximum level in use (1..MAX_LEVEL)

    // Simple deterministic RNG (good enough for skiplist leveling).
    uint32_t seed;
    uint32_t rng() {
        seed = seed * 1103515245u + 12345u;
        return seed;
    }

    int randomLevel() {
        int lvl = 1;
        while (lvl < MAX_LEVEL && (rng() & 1u)) ++lvl; // p=0.5 to go up
        return lvl;
    }

public:
    Skiplist() : head(new Node(-1, MAX_LEVEL)), curLevel(1), seed(712367u) {}

    bool search(int target) {
        Node* cur = head;
        for (int i = curLevel - 1; i >= 0; --i) {
            while (cur->next[i] && cur->next[i]->val < target) {
                cur = cur->next[i];
            }
        }
        cur = cur->next[0];
        return cur && cur->val == target;
    }

    void add(int num) {
        array<Node*, MAX_LEVEL> update{};
        Node* cur = head;

        for (int i = curLevel - 1; i >= 0; --i) {
            while (cur->next[i] && cur->next[i]->val < num) {
                cur = cur->next[i];
            }
            update[i] = cur;
        }

        int lvl = randomLevel();
        if (lvl > curLevel) {
            for (int i = curLevel; i < lvl; ++i) update[i] = head;
            curLevel = lvl;
        }

        Node* node = new Node(num, lvl);
        for (int i = 0; i < lvl; ++i) {
            node->next[i] = update[i]->next[i];
            update[i]->next[i] = node;
        }
    }

    bool erase(int num) {
        array<Node*, MAX_LEVEL> update{};
        Node* cur = head;

        for (int i = curLevel - 1; i >= 0; --i) {
            while (cur->next[i] && cur->next[i]->val < num) {
                cur = cur->next[i];
            }
            update[i] = cur;
        }

        Node* target = update[0]->next[0];
        if (!target || target->val != num) return false;

        for (int i = 0; i < curLevel; ++i) {
            if (update[i]->next[i] == target) {
                update[i]->next[i] = target->next[i];
            }
        }
        delete target;

        while (curLevel > 1 && head->next[curLevel - 1] == nullptr) {
            --curLevel;
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
// @lc code=end
