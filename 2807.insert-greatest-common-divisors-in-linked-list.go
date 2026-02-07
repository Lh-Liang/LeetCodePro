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
        a, b = b, a%b
    }
    return a
}

func insertGreatestCommonDivisors(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return head
    }
    curr := head
    for curr != nil && curr.Next != nil {
        v1 := curr.Val
        v2 := curr.Next.Val
        g := gcd(v1, v2)
        node := &ListNode{Val: g, Next: curr.Next}
        curr.Next = node
        curr = node.Next
    }
    // Optional verification step: check that all nodes are linked correctly (could be implemented if needed)
    return head
}
# @lc code=end