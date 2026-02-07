#
# @lc app=leetcode id=3743 lang=golang
#
# [3743] Maximize Cyclic Partition Score
#

# @lc code=start
func maximumScore(nums []int, k int) int64 {
    n := len(nums)
    extended := append(nums, nums...)
    dp := make([][]int64, k+1)
    for i := range dp {
        dp[i] = make([]int64, n*2)
    }
    
    for i := 0; i < n*2; i++ {
        for parts := 1; parts <= k; parts++ {
            if parts == 1 {
                maxNum := int64(extended[i])
                minNum := int64(extended[i])
                for j := i; j >= 0 && j > i-n; j-- {
                    maxNum = max(maxNum, int64(extended[j]))
                    minNum = min(minNum, int64(extended[j]))
                    dp[parts][i] = max(dp[parts][i], maxNum-minNum)
                }
            } else {
                maxNum := int64(extended[i])
                minNum := int64(extended[i])
                for j := i - 1; j >= 0 && j > i-n; j-- {
                    maxNum = max(maxNum, int64(extended[j]))
                    minNum = min(minNum, int64(extended[j]))
                    dp[parts][i] = max(dp[parts][i], dp[parts-1][j]+maxNum-minNum)
                }
            }
        }
    }
    
    result := int64(0)
    for i := n-1; i < n*2-1; i++ {
        result = max(result, dp[k][i])
    }
    return result
}
the
func max(a, b int64) int64 { if a > b { return a } else { return b } }
the
func min(a, b int64) int64 { if a < b { return a } else { return b } }
the 
dp code=end