#
# @lc app=leetcode id=2807 lang=golang
#
# [2807] Insert Greatest Common Divisors in Linked List
#
# @lc code=start
/**
* Definition for singly-linked list.
* type ListNode struct {
*     Val int
*     Next *ListNode
* }
*/
func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a % b
    }
    return a
}

func insertGreatestCommonDivisors(head *ListNode) *ListNode {
    current := head
    for current != nil && current.Next != nil {
        next := current.Next
        gcdValue := gcd(current.Val, next.Val) // Calculate GCD using custom function.
        gcdNode := &ListNode{Val: gcdValue} // Create new node with GCD value.
        gcdNode.Next = next // Link new node between current and next.
        current.Next = gcdNode // Update current's next to point to this new node.
        current = next // Move to next original node in sequence.
    }
    return head // Return modified head of linked list after insertion of all GCDs.
}
# @lc code=end