#
# @lc app=leetcode id=3686 lang=golang
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
func countStableSubsequences(nums []int) int {
    const MOD = 1e9 + 7
    n := len(nums)
    if n == 0 {
        return 0
    }
    
    dp := make([][2]int, n+1)
    dp[0][0] = 1 // Base case for parity transitions.
    total := int64(0)
    
    for i := range nums {
        parity := nums[i] % 2 // Determine current number's parity.
        
        // Calculate new subsequences ending at position i with current number's parity.
        dp[i+1][parity] = (dp[i][parity^1] + dp[i][parity]) % MOD // Extend both parities without forming invalid triples.
        
        // Correct potential overcount by checking for three consecutive same parity numbers.
        if i >= 2 && nums[i-1]%2 == parity && nums[i-2]%2 == parity {
            dp[i+1][parity] = (dp[i+1][parity] - dp[i-2][parity^1] + MOD) % MOD // Subtract invalid cases correctly.
        }
        
        // Update overall result by adding new valid subsequences ending at current index.
        total = (total + dp[i+1][parity]) % MOD
    }
    return int(total)
}
# @lc code=end