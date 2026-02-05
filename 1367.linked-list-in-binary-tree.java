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
* }
*/
class Solution {
    public boolean isSubPath(ListNode head, TreeNode root) {
        if (root == null) return false;
        // Check from this node, or from left subtree, or right subtree
        return checkPath(head, root) || isSubPath(head, root.left) || isSubPath(head, root.right);
    }
    // Helper function to check if list matches from this tree node
    private boolean checkPath(ListNode head, TreeNode node) {
        if (head == null) return true; // Finished list: success
        if (node == null) return false; // Finished tree, list not done: fail
        if (head.val != node.val) return false;
        // Try to match next list node with left or right child
        return checkPath(head.next, node.left) || checkPath(head.next, node.right);
    }
}
# @lc code=end