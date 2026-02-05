# @lc app=leetcode id=1670 lang=java
#
# [1670] Design Front Middle Back Queue
#
# @lc code=start
import java.util.ArrayList;
class FrontMiddleBackQueue {
    private ArrayList<Integer> left;
    private ArrayList<Integer> right;
    public FrontMiddleBackQueue() {
        this.left = new ArrayList<>();
        this.right = new ArrayList<>();
    }
    
    public void pushFront(int val) {
        left.add(0, val);
        balance();
    }
    
    public void pushMiddle(int val) {
        if (left.size() > right.size()) {
            right.add(0, left.remove(left.size() - 1));
        }
        left.add(val);
        balance();
    }
    
    public void pushBack(int val) {
        right.add(val);
        balance();
    }
    
    public int popFront() {
        if (left.isEmpty() && right.isEmpty()) return -1;
        int result = !left.isEmpty() ? left.remove(0) : right.remove(0);
        balance();
        return result;
    }
    
    public int popMiddle() {	
        if (left.isEmpty() && right.isEmpty()) return -1;													
        int result;		
        if (left.size() >= right.size()) {	
            result = left.remove(left.size() - 1);		
        } else {		
            result = right.remove(0);		
        }						
        balance();	
        return result;	}	
   	public int popBack() { 	if (right.isEmpty() && left.isEmpty()) return -1; 	int result = !right.isEmpty() ? right.remove(right.size() - 1) : left.remove(left.size() - 1); 	balance(); 	return result; }	private void balance(){while(left.size()>right.size()+1){right.add(0,left.remove(left.size()-1));}while(right.size()>left.size()){left.add(right.remove(0));}}
}
# @lc code=end