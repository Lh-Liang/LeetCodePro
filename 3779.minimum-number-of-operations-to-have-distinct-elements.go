#
# @lc app=leetcode id=3779 lang=golang
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#
# @lc code=start
func minOperations(nums []int) int {
    // Step 1: Early exit if all elements are already distinct
    seen := make(map[int]struct{})
    for _, v := range nums {
        seen[v] = struct{}{}
    }
    if len(seen) == len(nums) {
        return 0
    }
    op := 0
    for len(nums) > 0 {
        // Step 2a: Check for duplicates in the current array
        freq := make(map[int]struct{})
        hasDuplicate := false
        for _, v := range nums {
            if _, ok := freq[v]; ok {
                hasDuplicate = true
                break
            }
            freq[v] = struct{}{}
        }
        if !hasDuplicate {
            break
        }
        // Step 2b: Remove the first three elements, or all if fewer than 3
        if len(nums) <= 3 {
            nums = []int{}
        } else {
            nums = nums[3:]
        }
        op++
        // Step 2c: State verified by loop condition
    }
    // Step 4: Return the number of operations performed
    return op
}
# @lc code=end