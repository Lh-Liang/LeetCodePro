#
# @lc app=leetcode id=2058 lang=golang
#
# [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
#
# @lc code=start
/**
* Definition for singly-linked list.
* type ListNode struct {
*     Val int
*     Next *ListNode
* }
*/
func nodesBetweenCriticalPoints(head *ListNode) []int {
    indices := []int{}
    pos := 1
    prev := head
    curr := head.Next
    for curr != nil && curr.Next != nil {
        next := curr.Next
        if (curr.Val > prev.Val && curr.Val > next.Val) || (curr.Val < prev.Val && curr.Val < next.Val) {
            indices = append(indices, pos)
        }
        prev = curr
        curr = next
        pos++
    }
    if len(indices) < 2 {
        return []int{-1, -1}
    }
    minDist := indices[1] - indices[0]
    maxDist := indices[len(indices)-1] - indices[0]
    for i := 2; i < len(indices); i++ {
        if indices[i] - indices[i-1] < minDist {
            minDist = indices[i] - indices[i-1]
        }
    }
    return []int{minDist, maxDist}
}
# @lc code=end