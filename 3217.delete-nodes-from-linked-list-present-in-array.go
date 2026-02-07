#
# @lc app=leetcode id=3217 lang=golang
#
# [3217] Delete Nodes From Linked List Present in Array
#
# @lc code=start
/**
* Definition for singly-linked list.
* type ListNode struct {
*     Val int
*     Next *ListNode
* }
*/
func modifiedList(nums []int, head *ListNode) *ListNode {
    numSet := make(map[int]struct{}, len(nums))
    for _, num := range nums {
        numSet[num] = struct{}{}
    }
    dummy := &ListNode{Next: head}
    prev := dummy
    curr := head
    for curr != nil {
        if _, found := numSet[curr.Val]; found {
            prev.Next = curr.Next
        } else {
            prev = curr
        }
        curr = curr.Next
    }
    return dummy.Next
}
# @lc code=end