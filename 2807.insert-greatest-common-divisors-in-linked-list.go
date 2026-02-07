#
# @lc app=leetcode id=2807 lang=golang
#
# [2807] Insert Greatest Common Divisors in Linked List
#

# @lc code=start
import "math"

type ListNode struct {
    Val  int
    Next *ListNode
}

func insertGreatestCommonDivisors(head *ListNode) *ListNode {
    current := head
    for current != nil && current.Next != nil {
        gcdValue := math.Gcd(current.Val, current.Next.Val)
        newNode := &ListNode{Val: gcdValue, Next: current.Next}
        current.Next = newNode
        current = newNode.Next // Move two steps forward because one step goes to new node. 
    }
    return head
}
# @lc code=end