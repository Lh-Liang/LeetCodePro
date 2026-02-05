#
# @lc app=leetcode id=1367 lang=java
#
# [1367] Linked List in Binary Tree
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
/**
* Definition for a binary tree node.
* public class TreeNode {
*     int val;
*     TreeNode left;
*     TreeNode right;
*     TreeNode() {}
*     TreeNode(int val) { this.val = val; }
*     TreeNode(int val, TreeNode left, TreeNode right) {
*         this.val = val;
*         this.left = left;
*         this.right = right;
*     }
*/
class Solution {
    public boolean isSubPath(ListNode head, TreeNode root) {
        if (head == null) return true; // If linked list is empty, it matches by default.
        if (root == null) return false; // No more nodes to match against.
        // Try to match starting from current root or its children.
        return dfs(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right);
    }
    
    // Helper function to check path starting from specific tree node & list head.
    private boolean dfs(ListNode head, TreeNode root) {
        if (head == null) return true; // Entire LinkedList matched
        if (root == null || head.val != root.val) return false; // Mismatch or end of branch reached
        // Check both child paths recursively
        return dfs(head.next, root.left) || dfs(head.next, root.right);
    }
}
# @lc code=end