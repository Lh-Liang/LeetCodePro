#
# @lc app=leetcode id=3538 lang=golang
#
# [3538] Merge Operations for Minimum Travel Time
#

# @lc code=start
func minTravelTime(l int, n int, k int, position []int, time []int) int {
    // Initialize a DP table with large initial values.
    const INF = int(1e9)
    dp := make([][]int, k+1)
    for i := range dp {
        dp[i] = make([]int, n)
        for j := range dp[i] {
            dp[i][j] = INF
        }
    }

    // Base case: no merges -> compute direct travel time.
    dp[0][0] = 0 // Start with zero time at position 0.
    for i := 1; i < n; i++ {
        dist := position[i] - position[i-1]
        dp[0][i] = dp[0][i-1] + dist * time[i-1]
    }

    // Fill in the DP table for each merge operation up to k.
    for m := 1; m <= k; m++ {
        for i := m; i < n; i++ {
            // Attempt to merge every valid segment pair ending at i.
            for j := m - 1; j < i; j++ {
                dist := position[i] - position[j+1]
                newTime := time[j+1] + time[i]
                dp[m][i] = min(dp[m][i], dp[m-1][j+1] + dist * newTime)
            }
        }
    }

    // The answer is the minimum travel time with exactly k merges at the last position.
    return dp[k][n-1]
}

func min(a, b int) int {
    if a < b {
        return a
    }
    return b
}
# @lc code=end