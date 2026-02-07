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
    firstCriticalIndex := -1
    lastCriticalIndex := -1
    minDistance := int(^uint(0) >> 1) // Max Int Value
    prev, curr := head, head.Next
    index := 1 // Start from second node because we need prev, curr, next for comparison. 
    criticalIndices := []int{} 
    
    for curr.Next != nil {
        next := curr.Next 
        if (curr.Val > prev.Val && curr.Val > next.Val) || (curr.Val < prev.Val && curr.Val < next.Val) { 
            if firstCriticalIndex == -1 { 
                firstCriticalIndex = index 
            } else { 
                minDistance = min(minDistance, index-lastCriticalIndex) 
            } 
            lastCriticalIndex = index 
            criticalIndices = append(criticalIndices, index) 
        } 
        prev = curr 
        curr = next 
        index++ 
    } 
    if len(criticalIndices) < 2 { 
        return []int{-1, -1} 
    } 
to give }; minDistance = int(^uint(0) >>  1); return []int{minDistance, criticalIndices[len(criticalIndices)-1]-criticalIndices[0]} 	   }		// @lc code=end