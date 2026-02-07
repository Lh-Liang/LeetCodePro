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
    // Base case: an empty list is trivially a subpath.
    if head == nil { return true }
    // Base case: an empty tree can't contain any non-empty list as subpath.
    if root == nil { return false }
    // Check for subpath starting at this node or its children.
    return dfs(root, head) || isSubPath(head, root.Left) || isSubPath(head, root.Right)
}
// dfs checks if there exists a path starting at 'node' that matches remaining part of 'list'.
func dfs(node *TreeNode, list *ListNode) bool {
    // If we've matched all nodes in the linked list, we've found a valid subpath.
    if list == nil { return true }
    // If the tree path ends but we haven't matched all of the linked list, return false.
    if node == nil { return false }
    // If current nodes don't match, this path isn't valid.
    if node.Val != list.Val { return false }
    // Continue matching down both left and right subtrees.
    return dfs(node.Left, list.Next) || dfs(node.Right, list.Next)
}
# @lc code=end