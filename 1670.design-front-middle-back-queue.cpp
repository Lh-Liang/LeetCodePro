#
# @lc app=leetcode id=1670 lang=cpp
#
# [1670] Design Front Middle Back Queue
#
# @lc code=start
#include <deque>
class FrontMiddleBackQueue {
public:
    std::deque<int> left, right;
    FrontMiddleBackQueue() { }
    void rebalance() {
        while (left.size() > right.size() + 1) {
            right.push_front(left.back());
            left.pop_back();
        }
        while (left.size() < right.size()) {
            left.push_back(right.front());
            right.pop_front();
        }
    }
    void pushFront(int val) {
        left.push_front(val);
        rebalance();
    }
    void pushMiddle(int val) {
        if (left.size() > right.size()) {
            right.push_front(left.back());
            left.pop_back();
        }
        left.push_back(val);
    }
    void pushBack(int val) {
        right.push_back(val);
        rebalance();
    }
    int popFront() {
        if (left.empty() && right.empty()) return -1;
        int res;
        if (!left.empty()) {
            res = left.front();
            left.pop_front();
        } else {
            res = right.front();
            right.pop_front();
        }
        rebalance();
        return res;
    }
    int popMiddle() {
        if (left.empty() && right.empty()) return -1;
        int res = left.back();
        left.pop_back();
        rebalance();
        return res;
    }
    int popBack() {
        if (left.empty() && right.empty()) return -1;
        int res;
        if (!right.empty()) {
            res = right.back();
            right.pop_back();
        } else {
            res = left.back();
            left.pop_back();
        }
        rebalance();
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