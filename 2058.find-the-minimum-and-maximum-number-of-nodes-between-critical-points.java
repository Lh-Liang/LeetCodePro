#
# @lc app=leetcode id=2058 lang=java
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#
# @lc code=start
/**
* Definition for singly-linked list.
* public class ListNode {
*     int val;
*     ListNode next;
*     ListNode() {}
*     ListNode(int val) { this.val = val; }
*     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
* }
*/
class Solution {
    public int[] nodesBetweenCriticalPoints(ListNode head) {
        if (head == null || head.next == null || head.next.next == null) return new int[]{-1, -1};
        int minDist = Integer.MAX_VALUE;
        int firstCPIndex = -1;
        int lastCPIndex = -1;
        int index = 1; // Start from second node as we need at least one prev node
        List<Integer> cpIndices = new ArrayList<>(); 
        ListNode prev = head, curr = head.next; 
        while (curr != null && curr.next != null) { 
            if ((curr.val > prev.val && curr.val > curr.next.val) || (curr.val < prev.val && curr.val < curr.next.val)) { 
                if (firstCPIndex == -1) firstCPIndex = index; 
                else minDist = Math.min(minDist, index - lastCPIndex); 
                lastCPIndex = index; 
                cpIndices.add(index); 
            } 
            index++; 
            prev = curr; 
            curr = curr.next; 
        } 
        if (cpIndices.size() < 2) return new int[]{-1, -1};	else return new int[]{minDist, cpIndices.get(cpIndices.size()-1) - firstCPIndex};	}	}	# @lc code=end