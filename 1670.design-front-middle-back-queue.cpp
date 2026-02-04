# @lc app=leetcode id=1670 lang=cpp
# [1670] Design Front Middle Back Queue
#
# @lc code=start
#include <deque>
using namespace std;

class FrontMiddleBackQueue {
private:
    deque<int> front;
    deque<int> back;
    
    void balance() {
        // Ensure that front does not have more than one extra element than back
        if (front.size() > back.size() + 1) {
            back.push_front(front.back());
            front.pop_back();
        } else if (back.size() > front.size()) {
            front.push_back(back.front());
            back.pop_front();
        }
    }
    
public:
    FrontMiddleBackQueue() {
        
    }
    
    void pushFront(int val) {
        front.push_front(val);
        balance();																	
    }	 	 	 	 	 	 	 	 	 	 	  void pushMiddle(int val) {           // Insert into middle by pushing into front when equal or more elements in front       if (front.size() >= back.size()) {           front.push_back(val);       } else {           back.push_front(val);       }       balance();     }      void pushBack(int val) {         back.push_back(val);         balance();     }      int popFront() {         if (front.empty() && back.empty()) return -1;         int val = front.empty() ? back.front() : front.front();         if (!front.empty()) {             front.pop_front();         } else {             back.pop_front();         }         balance();         return val;     }      int popMiddle() {         if (front.empty() && back.empty()) return -1;         int val = (front.size() > back.size()) ? front.back() : back.front();         if (front.size() > back.size()) {             front.pop_back();         } else {             back.pop_front();         }         balance();         return val;     }      int popBack() {         if (back.empty() && front.empty()) return -1;         int val = !back.empty() ? back.back() : front.back();         if (!back.empty()) {             back.pop_back();         } else {             front.pop_back();         }         balance();         return val;     }};
t