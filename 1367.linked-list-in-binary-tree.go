#
# @lc app=leetcode id=1367 lang=golang
#
# [1367] Linked List in Binary Tree
#

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
    if root == nil {
        return false
    }
    if match(head, root) {
        return true
    }
    return isSubPath(head, root.Left) || isSubPath(head, root.Right)
}

func match(head *ListNode, node *TreeNode) bool {
    if head == nil {
        return true
    }
    if node == nil {
        return false
    }
    if node.Val != head.Val {
        return false
    }
    return match(head.Next, node.Left) || match(head.Next, node.Right)
}
# @lc code=end