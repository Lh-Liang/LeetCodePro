#
# @lc app=leetcode id=3640 lang=golang
#
# [3640] Trionic Array II
#

# @lc code=start
func maxSumTrionic(nums []int) int64 {
    n := len(nums)
    if n < 4 { return 0 } // as per constraints n >= 4
    
    inc := make([]int64, n) // increasing till here
    dec := make([]int64, n) // decreasing till here
    inc2 := make([]int64, n) // second increasing till here
    
    // Fill inc array - max sum ending with nums[i]
    inc[0] = int64(nums[0])
    for i := 1; i < n; i++ {
        if nums[i] > nums[i-1] {
            inc[i] = inc[i-1] + int64(nums[i])
        } else {
            inc[i] = int64(nums[i])
        }
    }
    
    // Fill dec array - max sum ending with nums[i]
    dec[n-1] = int64(nums[n-1])
    for i := n-2; i >= 0; i-- {
        if nums[i] > nums[i+1] {
            dec[i] = dec[i+1] + int64(nums[i])
        } else {
            dec[i] = int64(nums[i])
        }
    }
    
    // Fill inc2 array - max sum ending with nums[i]
    inc2[n-1] = int64(nums[n-1])
    for i := n-2; i >= 0; i-- {
        if nums[i] < nums[i+1] {
            inc2[i] = inc2[i+1] + int64(nums[i])
        } else {
            inc2[i] = int64(nums[i])
        }
    }