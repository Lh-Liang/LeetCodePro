#
# @lc app=leetcode id=3686 lang=golang
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
func countStableSubsequences(nums []int) int {
    const MOD = 1000000007
    n := len(nums)
    if n == 0 { return 0 }
    dp := make([][2]int, n+1) // dp[i][0] = count ending with even; dp[i][1] = count ending with odd
    var result int
    for i := 0; i < n; i++ {
        parity := nums[i] % 2
        if parity == 0 { // current number is even
            dp[i+1][0] = (dp[i][0] + 1) % MOD // extend even-ending sequences or start new with curr even number
            dp[i+1][1] = dp[i][1]
        } else { // current number is odd
            dp[i+1][1] = (dp[i][1] + 1) % MOD // extend odd-ending sequences or start new with curr odd number
            dp[i+1][0] = dp[i][0]
        }
        result = (result + dp[i+1][0] + dp[i+1][1]) % MOD // add all possible new stable subsequences ending at i+1
    }
    return result%MOD // return total count of stable subsequences mod 10^9 + 7 
}
# @lc code=end