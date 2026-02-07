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
    current := head
    carry := 0
    
    // Traverse the linked list and double each digit
    for current != nil {
        newValue := current.Val*2 + carry
        current.Val = newValue % 10
        carry = newValue / 10
        
        if current.Next == nil && carry > 0 {
            // If at end of list and there is carry, add new node
            current.Next = &ListNode{Val: carry}
            break
        }
        
        current = current.Next
    }
    
    return head
}
# @lc code=end