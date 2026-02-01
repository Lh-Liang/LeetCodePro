#
# @lc app=leetcode id=1670 lang=cpp
#
# [1670] Design Front Middle Back Queue
#
# @lc code=start
#include <deque>
using namespace std;

class FrontMiddleBackQueue {
    deque<int> left, right;

    void balance() {
        if (left.size() > right.size()) {
            right.push_front(left.back());
            left.pop_back();
        } else if (right.size() > left.size() + 1) {
            left.push_back(right.front());
            right.pop_front();
        }
    }

public:
    FrontMiddleBackQueue() {}

    void pushFront(int val) {
        left.push_front(val);
        balance();
    }

    void pushMiddle(int val) {
        if (left.size() == right.size()) {
            right.push_front(val);
        } else {
            left.push_back(val);
        }
    }

    void pushBack(int val) {
        right.push_back(val);
        balance();
    }

    int popFront() {
        if (left.empty() && right.empty()) return -1;
        int val;
        if (left.empty()) {
            val = right.front();
            right.pop_front();
        } else {
            val = left.front();
            left.pop_front();
        }
        balance();
        return val;
    }

    int popMiddle() {
        if (left.empty() && right.empty()) return -1;
        int val;
        if (left.size() == right.size()) {
            val = left.back();
            left.pop_back();
        } else {
            val = right.front();
            right.pop_front();
        }
        return val;
    }

    int popBack() {
        if (right.empty()) return -1;
        int val = right.back();
        right.pop_back();
        balance();
        return val;
    }
};
# @lc code=end