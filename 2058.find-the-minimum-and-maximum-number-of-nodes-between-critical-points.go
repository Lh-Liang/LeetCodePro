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
    if head == nil || head.Next == nil || head.Next.Next == nil {
        return []int{-1, -1}
    }
    prev := head.Val
    index := 1
    firstCriticalPoint := -1
    lastCriticalPoint := -1
    minDistance := int(^uint(0) >> 1) // Initialize to max int value
    maxDistance := -1
    current := head.Next
    for current != nil && current.Next != nil {
        if (current.Val > prev && current.Val > current.Next.Val) || 
           (current.Val < prev && current.Val < current.Next.Val) {
            if firstCriticalPoint == -1 { // First critical point found.
                firstCriticalPoint = index
            } else { // Calculate distances for subsequent critical points.
                minDistance = min(minDistance, index-lastCriticalPoint)
                maxDistance = index-firstCriticalPoint 
            }
            lastCriticalPoint = index 
        }
        prev = current.Val 
        current = current.Next 
        index++ 
    }
    if minDistance == int(^uint(0) >> 1) {
        return []int{-1,-1} 
    }
    return []int{minDistance,maxDistance} 
}
func min(a,b int) int { 
    if a < b { return a } 
    return b 
}
# @lc code=end