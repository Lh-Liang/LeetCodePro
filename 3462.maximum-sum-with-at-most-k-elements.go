#
# @lc app=leetcode id=3462 lang=golang
#
# [3462] Maximum Sum With at Most K Elements
#

# @lc code=start
func maxSum(grid [][]int, limits []int, k int) int64 {
    n := len(grid)
    dp := make([]int64, k+1)
    for i := 0; i < n; i++ {
        row := grid[i]
        sort.Sort(sort.Reverse(sort.IntSlice(row)))
        prefix := make([]int64, limits[i]+1)
        for j := 1; j <= limits[i] && j <= len(row); j++ {
            prefix[j] = prefix[j-1] + int64(row[j-1])
        }
        ndp := make([]int64, k+1)
        copy(ndp, dp)
        for take := 1; take <= limits[i] && take <= len(row); take++ {
            for prev := 0; prev+take <= k; prev++ {
                if dp[prev] + prefix[take] > ndp[prev+take] {
                    ndp[prev+take] = dp[prev] + prefix[take]
                }
            }
        }
        dp = ndp
    }
    ans := int64(0)
    for i := 0; i <= k; i++ {
        if dp[i] > ans {
            ans = dp[i]
        }
    }
    return ans
}
# @lc code=end