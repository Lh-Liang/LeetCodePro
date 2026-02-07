# @lc app=leetcode id=3779 lang=golang
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#
# @lc code=start
func minOperations(nums []int) int {
    operations := 0
    
    for containsDuplicates(nums) {
        if len(nums) <= 3 {
            // Remove all remaining elements if fewer than three
            nums = []int{}
        } else {
            // Remove the first three elements
            nums = nums[3:]
        }
        operations++
    }
    
    return operations
}

func containsDuplicates(nums []int) bool {
    elementCount := make(map[int]bool)
    for _, num := range nums {
        if elementCount[num] {
            return true
        }
        elementCount[num] = true
    }
    return false
}
# @lc code=end