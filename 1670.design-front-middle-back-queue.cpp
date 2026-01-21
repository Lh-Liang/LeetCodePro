#
# @lc app=leetcode id=1670 lang=cpp
#
# [1670] Design Front Middle Back Queue
#

// @lc code=start
class FrontMiddleBackQueue {
private:
    deque<int> left, right;
    
    void balance() {
        // Maintain: left.size() == right.size() OR left.size() == right.size() + 1
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
            // Odd total: move current middle to right, then add new middle
            right.push_front(left.back());
            left.pop_back();
        }
        left.push_back(val);
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
        int val;
        if (right.empty()) {
            val = left.back();
            left.pop_back();
        } else {
            val = right.back();
            right.pop_back();
        }
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
// @lc code=end