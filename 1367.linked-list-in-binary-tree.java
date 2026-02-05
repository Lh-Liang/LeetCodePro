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
        if (root == null) return false;
        // Start DFS from each node to find a matching path
        return dfs(root, head) || isSubPath(head, root.left) || isSubPath(head, root.right);
    }
    
    private boolean dfs(TreeNode node, ListNode head) {
        if (head == null) return true; // LinkedList fully matched
        if (node == null) return false; // Reached end of path without full match
        if (node.val != head.val) return false; // Mismatch between tree and list nodes
        // Continue DFS on both children with next list node
        return dfs(node.left, head.next) || dfs(node.right, head.next);
    }
}
# @lc code=end