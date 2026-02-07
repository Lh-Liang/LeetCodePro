#
# @lc app=leetcode id=3434 lang=golang
#
# [3434] Maximum Frequency After Subarray Operation
#
# @lc code=start
func maxFrequency(nums []int, k int) int {
    n := len(nums)
    delta := make([]int, n)
    for i := 0; i < n; i++ {
        delta[i] = k - nums[i]
    }
    maxFreq := 0
    deltaGroups := make(map[int][]int)
    for i, d := range delta {
        deltaGroups[d] = append(deltaGroups[d], i)
    }
    for _, positions := range deltaGroups {
        // Find the largest contiguous segment in positions
        if len(positions) == 0 {
            continue
        }
        count := 1
        localMax := 1
        for i := 1; i < len(positions); i++ {
            if positions[i] == positions[i-1]+1 {
                count++
            } else {
                count = 1
            }
            if count > localMax {
                localMax = count
            }
        }
        if localMax > maxFreq {
            maxFreq = localMax
        }
    }
    return maxFreq
}
# @lc code=end