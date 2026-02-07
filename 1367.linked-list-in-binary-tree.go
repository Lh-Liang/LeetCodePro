# @lc app=leetcode id=1367 lang=golang

# [1367] Linked List in Binary Tree

# @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubPath(head *ListNode, root *TreeNode) bool {
    if head == nil { return true } // If head is nil, we've matched all nodes.
    if root == nil { return false } // If root is nil before matching all, fail.
    return dfs(head, root) || isSubPath(head, root.Left) || isSubPath(head, root.Right) 
}
// Helper function to check current path matches or not. 
func dfs(head *ListNode, node *TreeNode) bool { 
    if head == nil { return true } // All matched 
    if node == nil { return false } // Path ends without full match 
    if head.Val != node.Val { return false }  // Values do not match 
    return dfs(head.Next, node.Left) || dfs(head.Next, node.Right) 
}
# @lc code=end