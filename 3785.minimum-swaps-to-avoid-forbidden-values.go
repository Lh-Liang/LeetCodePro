#
# @lc app=leetcode id=3785 lang=golang
#
# [3785] Minimum Swaps to Avoid Forbidden Values
#

# @lc code=start
func minSwaps(nums []int, forbidden []int) int {
    n := len(nums)
    swapCount := 0
    conflictIndices := make([]int, 0)
    nonConflictIndices := make(map[int]bool)
    
    for i := 0; i < n; i++ {
        if nums[i] == forbidden[i] {
            conflictIndices = append(conflictIndices, i)
        } else {
            nonConflictIndices[i] = true
        }
    }
    
    if len(conflictIndices) == 0 {
        return 0
    }

    for _, ci := range conflictIndices {
        foundSwap := false
        for ai := range nonConflictIndices {
            if nums[ai] != forbidden[ci] && nums[ci] != forbidden[ai] {
                nums[ci], nums[ai] = nums[ai], nums[ci]
                delete(nonConflictIndices, ai)
                swapCount++
                foundSwap = true
                break
            }
        }
        if !foundSwap {
            return -1
        }
    }
    return swapCount
}
# @lc code=end