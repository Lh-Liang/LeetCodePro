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
    var indices []int
    var prev *ListNode = nil
    var curr = head
    position := 0
    
    for curr != nil && curr.Next != nil {
        if prev != nil {
            if (curr.Val > prev.Val && curr.Val > curr.Next.Val) || (curr.Val < prev.Val && curr.Val < curr.Next.Val) {
                indices = append(indices, position)
            }
        }
        prev = curr
        curr = curr.Next
        position++
    }
    
    if len(indices) < 2 {
        return []int{-1, -1}
    }
    
    minDistance := indices[1] - indices[0]
    maxDistance := indices[len(indices)-1] - indices[0]
   
   for i := 1; i < len(indices); i++ { 
       if indices[i] - indices[i-1] < minDistance { 
           minDistance = indices[i] - indices[i-1] 
       } 
   } 
   return []int{minDistance, maxDistance} 
}
# @lc code=end