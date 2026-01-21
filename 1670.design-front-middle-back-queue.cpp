#include <deque>
using namespace std;

/*
 * @lc app=leetcode id=1670 lang=cpp
 *
 * [1670] Design Front Middle Back Queue
 */

// @lc code=start
class FrontMiddleBackQueue {
    deque<int> L, R;

    void rebalance() {
        while ((int)L.size() > (int)R.size() + 1) {
            R.push_front(L.back());
            L.pop_back();
        }
        while ((int)L.size() < (int)R.size()) {
            L.push_back(R.front());
            R.pop_front();
        }
    }

public:
    FrontMiddleBackQueue() {}

    void pushFront(int val) {
        L.push_front(val);
        rebalance();
    }

    void pushMiddle(int val) {
        if ((int)L.size() > (int)R.size()) {
            R.push_front(L.back());
            L.pop_back();
        }
        L.push_back(val);
        rebalance();
    }

    void pushBack(int val) {
        R.push_back(val);
        rebalance();
    }

    int popFront() {
        if (L.empty() && R.empty()) return -1;
        int ret = L.front();
        L.pop_front();
        rebalance();
        return ret;
    }

    int popMiddle() {
        if (L.empty() && R.empty()) return -1;
        int ret = L.back();
        L.pop_back();
        rebalance();
        return ret;
    }

    int popBack() {
        if (L.empty() && R.empty()) return -1;
        int ret;
        if (!R.empty()) {
            ret = R.back();
            R.pop_back();
        } else {
            ret = L.back();
            L.pop_back();
        }
        rebalance();
        return ret;
    }
};
// @lc code=end
