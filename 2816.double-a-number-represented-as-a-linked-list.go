#
# @lc app=leetcode id=2816 lang=golang
#
# [2816] Double a Number Represented as a Linked List
#

# @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func doubleIt(head *ListNode) *ListNode {
    // Helper to reverse a singly linked list
    reverse := func(node *ListNode) *ListNode {
        var prev *ListNode = nil
        for node != nil {
            next := node.Next
            node.Next = prev
            prev = node
            node = next
        }
        return prev
    }
    // Step 1: reverse the list
    head = reverse(head)
    carry := 0
    curr := head
    var prev *ListNode = nil
    // Step 2: double each node and handle carry
    for curr != nil {
        sum := curr.Val * 2 + carry
        curr.Val = sum % 10
        carry = sum / 10
        prev = curr
        curr = curr.Next
    }
    // Step 3: handle leftover carry
    if carry > 0 {
        prev.Next = &ListNode{Val: carry}
    }
    // Step 4: reverse again to restore original order
    return reverse(head)
}
# @lc code=end