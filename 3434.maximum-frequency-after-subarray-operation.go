#
# @lc app=leetcode id=3434 lang=golang
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
func maxFrequency(nums []int, k int) int {
    // Sort nums to allow efficient evaluation of subarrays
    sort.Ints(nums)
    left := 0
    sum := 0 // To store sum of elements within current window
    maxFreq := 0 // To store maximum frequency found
    // Iterate over nums with right as end of sliding window
    for right := 0; right < len(nums); right++ {
        sum += nums[right] // Add current element to sum
        // Check if we can transform current window into nums[right]
        while nums[right]*(right-left+1)-sum > k {
            sum -= nums[left] // Remove leftmost element from sum
            left++ // Move left pointer forward
        }
        // Update max frequency if current window is valid
        maxFreq = max(maxFreq, right-left+1)
    }
    return maxFreq // Return maximum frequency found
}
// Helper function to determine max of two integers
func max(a, b int) int { if a > b { return a } else { return b }}
# @lc code=end