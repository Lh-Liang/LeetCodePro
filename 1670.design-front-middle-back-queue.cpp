#
# @lc app=leetcode id=1670 lang=cpp
#
# [1670] Design Front Middle Back Queue
#

# @lc code=start
#include <deque>
using namespace std;
class FrontMiddleBackQueue {
public:
    deque<int> dq;
    FrontMiddleBackQueue() { }
    void pushFront(int val) { dq.push_front(val); }
    void pushMiddle(int val) { 
        int mid = dq.size() / 2; 
        dq.insert(dq.begin() + mid, val); 
    }
    void pushBack(int val) { dq.push_back(val); }
    int popFront() { 
        if(dq.empty()) return -1; 
        int val = dq.front(); 
        dq.pop_front(); 
        return val; 
    }
    int popMiddle() { 
        if(dq.empty()) return -1; 
        int mid = (dq.size() - 1) / 2; 
        auto it = dq.begin() + mid; 
        int val = *it; 
        dq.erase(it); 
        return val; 
    }
    int popBack() { 
        if(dq.empty()) return -1; 
        int val = dq.back(); 
        dq.pop_back(); 
        return val; 
    }
};
done