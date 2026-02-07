#
# @lc app=leetcode id=3510 lang=golang
#
# [3510] Minimum Pair Removal to Sort Array II
#

# @lc code=start
func minimumPairRemoval(nums []int) int {
    ops := 0
    for len(nums) > 1 {
        n := len(nums)
        minSum := int(^uint(0) >> 1) 
        minIndex := -1
        for i := 0; i < n-1; i++ {
            sum := nums[i] + nums[i+1]
            if sum < minSum {
                minSum = sum
                minIndex = i
            }
        }
        if minIndex != -1 {
            nums[minIndex] = minSum
            nums = append(nums[:minIndex+1], nums[minIndex+2:]...)
            ops++
        }
        if isNonDecreasing(nums) { 
            break
        }
    }
    return ops
}

func isNonDecreasing(arr []int) bool {
    for i := 0; i < len(arr)-1; i++ {
        if arr[i] > arr[i+1] {
            return false
        }
    }
    return true
}
# @lc code=end