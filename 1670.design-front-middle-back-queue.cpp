#
# @lc app=leetcode id=1670 lang=cpp
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
#include <deque>

class FrontMiddleBackQueue {
private:
    std::deque<int> left;
    std::deque<int> right;

    // Maintains the invariant: left.size() == right.size() or left.size() == right.size() + 1
    void balance() {
        if (left.size() > right.size() + 1) {
            right.push_front(left.back());
            left.pop_back();
        } else if (right.size() > left.size()) {
            left.push_back(right.front());
            right.pop_front();
        }
    }

public:
    FrontMiddleBackQueue() {
        
    }
    
    void pushFront(int val) {
        left.push_front(val);
        balance();
    }
    
    void pushMiddle(int val) {
        if (left.size() > right.size()) {
            right.push_front(left.back());
            left.pop_back();
        }
        left.push_back(val);
        // No balance needed theoretically, but safe to call or rely on logic
        // If L=k+1, R=k -> move -> L=k, R=k+1 -> push -> L=k+1, R=k+1. Balanced.
        // If L=k, R=k -> push -> L=k+1, R=k. Balanced.
    }
    
    void pushBack(int val) {
        right.push_back(val);
        balance();
    }
    
    int popFront() {
        if (left.empty()) return -1;
        int val = left.front();
        left.pop_front();
        balance();
        return val;
    }
    
    int popMiddle() {
        if (left.empty()) return -1;
        int val = left.back();
        left.pop_back();
        balance();
        return val;
    }
    
    int popBack() {
        if (left.empty()) return -1;
        // If right is empty, then left must have exactly 1 element (due to invariant)
        if (right.empty()) {
            int val = left.back();
            left.pop_back();
            return val;
        }
        int val = right.back();
        right.pop_back();
        balance();
        return val;
    }
};

/**
 * Your FrontMiddleBackQueue object will be instantiated and called as such:
 * FrontMiddleBackQueue* obj = new FrontMiddleBackQueue();
 * obj->pushFront(val);
 * obj->pushMiddle(val);
 * obj->pushBack(val);
 * int param_4 = obj->popFront();
 * int param_5 = obj->popMiddle();
 * int param_6 = obj->popBack();
 */
# @lc code=end