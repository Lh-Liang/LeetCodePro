#
# @lc app=leetcode id=3621 lang=golang
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
func popcountDepth(n int64, k int) int64 {
    // Dynamic programming map to store calculated depths
    dp := make(map[int64]int)
    var count int64 = 0
    
    // Helper function to calculate popcount-depth recursively with memoization
    var calcDepth func(int64) int
    calcDepth = func(x int64) int {
        if x == 1 {
            return 0
        }
        if d, found := dp[x]; found {
            return d
        }
        nextX := int64(bits.OnesCount(uint(x)))
        dp[x] = 1 + calcDepth(nextX)
        return dp[x]
    }
    
    // Check all numbers from 1 to n
    for x := int64(1); x <= n; x++ {
        if calcDepth(x) == k {
            count++
        }
    }
    return count
}
// @lc code=end