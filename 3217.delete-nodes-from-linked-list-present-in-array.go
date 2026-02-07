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
    // Convert nums to a set for O(1) lookup time
    numSet := make(map[int]bool)
    for _, num := range nums {
        numSet[num] = true
    }
    
    // Use a dummy node to handle edge cases easily
    dummy := &ListNode{Next: head}
    current := dummy
    
    // Iterate through the linked list and remove nodes present in numSet
    for current.Next != nil {
        if numSet[current.Next.Val] {
            // Skip over nodes that are in numSet (remove them)
            current.Next = current.Next.Next
        } else {
            // Otherwise, move to the next node normally
            current = current.Next
        }
    }
    
    return dummy.Next // Return the new head of the list after removals are done
}
# @lc code=end