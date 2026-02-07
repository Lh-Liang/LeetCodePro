# @lc code=start
#include <deque>
using namespace std;

class FrontMiddleBackQueue {
private:
    deque<int> front;
    deque<int> back;

    void balance() {
        if (front.size() > back.size() + 1) {
            back.push_front(front.back());
            front.pop_back();
        } else if (back.size() > front.size()) {
            front.push_back(back.front());
            back.pop_front();
        }
    }

public:
    FrontMiddleBackQueue() {}
    
    void pushFront(int val) {
        front.push_front(val);
        balance();
    }
    
    void pushMiddle(int val) {
        if (front.size() <= back.size()) {
            front.push_back(val);
        } else {
            back.push_front(val);
        }
        balance();
    }
    
    void pushBack(int val) {
        back.push_back(val);
        balance();
    }
    
    int popFront() {
        int res = -1;
        if (!front.empty()) {
            res = front.front();
            front.pop_front();
        } else if (!back.empty()) {
            res = back.front();
            back.pop_front();
        }
balance();return res;}int popMiddle(){int res=-1;if(front.size()==back.size()){res=front.back();front.pop_back();}else{res=back.front();back.pop_front();}balance();return res;}int popBack(){int res=-1;if(!back.empty()){res=back.back();back.pop_back();}else if(!front.empty()){res=front.back();front.pop_back();}balance();return res;}"}