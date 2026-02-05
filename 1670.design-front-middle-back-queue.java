#
# @lc app=leetcode id=1670 lang=java
#
# [1670] Design Front Middle Back Queue
#
# @lc code=start
import java.util.LinkedList;

class FrontMiddleBackQueue {
    LinkedList<Integer> q;

    public FrontMiddleBackQueue() {
        q = new LinkedList<>();
    }

    public void pushFront(int val) {
        q.addFirst(val);
    }

    public void pushMiddle(int val) {
        int idx = q.size() / 2;
        q.add(idx, val);
    }

    public void pushBack(int val) {
        q.addLast(val);
    }

    public int popFront() {
        if (q.isEmpty()) return -1;
        return q.removeFirst();
    }

    public int popMiddle() {
        if (q.isEmpty()) return -1;
        int idx = (q.size() - 1) / 2;
        return q.remove(idx);
    }

    public int popBack() {
        if (q.isEmpty()) return -1;
        return q.removeLast();
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