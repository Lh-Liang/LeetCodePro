#
# @lc app=leetcode id=3420 lang=golang
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
func countNonDecreasingSubarrays(nums []int, k int) int64 {
    n := len(nums)
    result := int64(0)
    left := 0
    currentOperations := 0
    for right := 1; right < n; right++ {
        if nums[right] < nums[right-1] {
            currentOperations += nums[right-1] - nums[right]
        }
        while currentOperations > k && left < right {
            if nums[left+1] < nums[left] {
                currentOperations -= nums[left] - nums[left+1]
            }
            left++
        }
        result += int64(right - left)
    }
    result += int64(n) // each single element is a valid subarray
    return result
}
# @lc code=end