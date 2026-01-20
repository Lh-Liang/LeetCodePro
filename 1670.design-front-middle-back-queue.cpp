#
# @lc app=leetcode id=1670 lang=cpp
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
#include <deque>

class FrontMiddleBackQueue {
private:
    std::deque<int> dq1; // Front half
    std::deque<int> dq2; // Back half

    // Maintain invariant: dq2.size() == dq1.size() OR dq2.size() == dq1.size() + 1
    void balance() {
        if (dq1.size() > dq2.size()) {
            dq2.push_front(dq1.back());
            dq1.pop_back();
        } else if (dq2.size() > dq1.size() + 1) {
            dq1.push_back(dq2.front());
            dq2.pop_front();
        }
    }

public:
    FrontMiddleBackQueue() {
    }
    
    void pushFront(int val) {
        dq1.push_front(val);
        balance();
    }
    
    void pushMiddle(int val) {
        if (dq1.size() == dq2.size()) {
            dq2.push_front(val);
        } else {
            dq1.push_back(val);
        }
    }
    
    void pushBack(int val) {
        dq2.push_back(val);
        balance();
    }
    
    int popFront() {
        if (dq2.empty()) return -1;
        int res;
        if (dq1.empty()) {
            res = dq2.front();
            dq2.pop_front();
        } else {
            res = dq1.front();
            dq1.pop_front();
        }
        balance();
        return res;
    }
    
    int popMiddle() {
        if (dq2.empty()) return -1;
        int res;
        if (dq1.size() == dq2.size()) {
            res = dq1.back();
            dq1.pop_back();
        } else {
            res = dq2.front();
            dq2.pop_front();
        }
        balance();
        return res;
    }
    
    int popBack() {
        if (dq2.empty()) return -1;
        int res = dq2.back();
        dq2.pop_back();
        balance();
        return res;
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