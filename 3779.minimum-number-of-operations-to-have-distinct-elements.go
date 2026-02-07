#
# @lc app=leetcode id=3779 lang=golang
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
func minOperations(nums []int) int {
    operationCount := 0
    
    // Create a function to check if there are duplicates
    hasDuplicates := func(arr []int) bool {
        seen := make(map[int]bool)
        for _, num := range arr {
            if seen[num] {
                return true
            }
            seen[num] = true
        }
        return false
    }
    
    // Continue performing operations until there are no duplicates or list is empty
    for len(nums) > 0 && hasDuplicates(nums) {
        // Remove up to three elements from the start of nums
        if len(nums) >= 3 {
            nums = nums[3:]   // remove first three elements if possible
        } else {
            nums = []int{}   // clear all remaining if less than three left
        }
        operationCount++   // increment operation count after each removal operation
    }
    
    return operationCount  // return total number of operations performed 
}
# @lc code=end