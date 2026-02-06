#
# @lc app=leetcode id=1670 lang=java
#
# [1670] Design Front Middle Back Queue
#
# @lc code=start
import java.util.ArrayList;
class FrontMiddleBackQueue {
    ArrayList<Integer> q;
    public FrontMiddleBackQueue() {
        q = new ArrayList<>();
    }
    public void pushFront(int val) {
        q.add(0, val);
    }
    public void pushMiddle(int val) {
        int mid = q.size() / 2;
        q.add(mid, val);
    }
    public void pushBack(int val) {
        q.add(val);
    }
    public int popFront() {
        if (q.isEmpty()) return -1;
        return q.remove(0);
    }
    public int popMiddle() {
        if (q.isEmpty()) return -1;
        int mid = (q.size() - 1) / 2;
        return q.remove(mid);
    }
    public int popBack() {
        if (q.isEmpty()) return -1;
        return q.remove(q.size() - 1);
    }
}
/**
* Your FrontMiddleBackQueue object will be instantiated and called as such:
* FrontMiddleBackQueue obj = new FrontMiddleBackQueue();
* obj.pushFront(val);
* obj.pushMiddle(val);
* obj.pushBack(val);
* int param_4 = obj.popFront();
* int param_5 = obj.popMiddle();
* int param_6 = obj.popBack();
*/
# @lc code=end