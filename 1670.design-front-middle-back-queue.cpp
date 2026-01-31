#
# @lc app=leetcode id=1670 lang=cpp
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
#include <deque>

class FrontMiddleBackQueue {
    std::deque<int> q1, q2;

    // Maintain invariant: q1.size() <= q2.size() <= q1.size() + 1
    void balance() {
        if (q1.size() > q2.size()) {
            q2.push_front(q1.back());
            q1.pop_back();
        } else if (q2.size() > q1.size() + 1) {
            q1.push_back(q2.front());
            q2.pop_front();
        }
    }

public:
    FrontMiddleBackQueue() {
    }
    
    void pushFront(int val) {
        q1.push_front(val);
        balance();
    }
    
    void pushMiddle(int val) {
        if (q1.size() == q2.size()) {
            q2.push_front(val);
        } else {
            q1.push_back(val);
        }
        // balance() call is technically redundant here but safe
        balance();
    }
    
    void pushBack(int val) {
        q2.push_back(val);
        balance();
    }
    
    int popFront() {
        if (q1.empty() && q2.empty()) return -1;
        int val;
        if (q1.empty()) {
            val = q2.front();
            q2.pop_front();
        } else {
            val = q1.front();
            q1.pop_front();
        }
        balance();
        return val;
    }
    
    int popMiddle() {
        if (q1.empty() && q2.empty()) return -1;
        int val;
        if (q1.size() == q2.size()) {
            val = q1.back();
            q1.pop_back();
        } else {
            val = q2.front();
            q2.pop_front();
        }
        balance();
        return val;
    }
    
    int popBack() {
        if (q1.empty() && q2.empty()) return -1;
        int val = q2.back();
        q2.pop_back();
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