#
# @lc app=leetcode id=1670 lang=java
#
# [1670] Design Front Middle Back Queue
#
# @lc code=start
import java.util.Deque;
import java.util.LinkedList;

class FrontMiddleBackQueue {
    private Deque<Integer> frontDeque;
    private Deque<Integer> backDeque;
    
    public FrontMiddleBackQueue() {
        frontDeque = new LinkedList<>();
        backDeque = new LinkedList<>();
    }
    
    public void pushFront(int val) {
        frontDeque.addFirst(val);
        balance();
    }
    
    public void pushMiddle(int val) {
        if (frontDeque.size() > backDeque.size()) {
            backDeque.addFirst(frontDeque.removeLast());
        }
        frontDeque.addLast(val);
        balance();
    }
    
    public void pushBack(int val) {
        backDeque.addLast(val);
        balance();
    }
    
    public int popFront() {
        if (frontDeque.isEmpty() && backDeque.isEmpty()) return -1;
        int value = !frontDeque.isEmpty() ? frontDeque.removeFirst() : backDeque.removeFirst();
        balance();
        return value;
    }

    public int popMiddle() {		   		
		if (frontDeque.isEmpty() && backDeque.isEmpty()) return -1;		   		
		int value = (frontDeque.size() >= backDeque.size()) ? frontDeque.removeLast() : backDeque.removeFirst();		   		
		balance();		   		
		return value;		   	
}	

public int popBack() {  	  	   	   	  if (backDeque.isEmpty() && frontDeque.isEmpty()) return -1;  	  	   	   	  int value = !backDeque.isEmpty() ? backDeque.removeLast() : frontDeque.removeLast();  	balance(); return value; }  private void balance(){while(frontDequeue.size()>backDequeue.size()+1){backDequeue.addFirst(frontDequeue.removeLast());}while(backDequeue.size()>frontDequeue.size()){frontDequeue.addLast(backDequeue.removeFirst());}} # @lc code=end