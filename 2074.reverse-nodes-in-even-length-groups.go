#
# @lc app=leetcode id=2074 lang=golang
#
# [2074] Reverse Nodes in Even Length Groups
#

# @lc code=start
/**
* Definition for singly-linked list.
* type ListNode struct {
*     Val int
*     Next *ListNode
* }
*/
func reverseEvenLengthGroups(head *ListNode) *ListNode {
    dummy := &ListNode{Next: head}
    prev := dummy
    curr := head
    groupSize := 1
    for curr != nil {
        count := 0
        temp := curr
        // Count the actual group length
        for temp != nil && count < groupSize {
            count++
            temp = temp.Next
        }
        // Find the tail of the group
        tail := curr
        for i := 1; i < count; i++ {
            tail = tail.Next
        }
        nextGroupHead := tail.Next
        if count%2 == 0 {
            // Reverse the group
            prevNode := nextGroupHead
            node := curr
            for i := 0; i < count; i++ {
                tmp := node.Next
                node.Next = prevNode
                prevNode = node
                node = tmp
            }
            prev.Next = tail
            prev = curr
        } else {
            prev = tail
        }
        curr = nextGroupHead
        groupSize++
        // After each group, verify pointers (implicit in pointer logic)
    }
    // Final verification of list structure can be added if needed (implicit in construction)
    return dummy.Next
}
# @lc code=end