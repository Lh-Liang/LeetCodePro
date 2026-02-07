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
    carry := 0
    dummy := &ListNode{0, head}
    cur := head
    prev := dummy
    
    for cur != nil {
        sum := cur.Val*2 + carry
        cur.Val = sum % 10
        carry = sum / 10
        prev = cur
        cur = cur.Next
    }
    
    if carry > 0 {
        prev.Next = &ListNode{carry, nil}
    }
    
    return dummy.Next
}
# @lc code=end