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
    if b == 0 { return a } 
    return gcd(b, a % b) 
}
func insertGreatestCommonDivisors(head *ListNode) *ListNode {
    current := head 
    for current != nil && current.Next != nil { 
        gcdValue := gcd(current.Val, current.Next.Val) 
        newNode := &ListNode{Val: gcdValue} 
        newNode.Next = current.Next 
        current.Next = newNode 
        current = newNode.Next 
    } 
    return head 
}
# @lc code=end