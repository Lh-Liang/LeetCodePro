#
# @lc app=leetcode id=3686 lang=golang
#
# [3686] Number of Stable Subsequences
#
# @lc code=start
func countStableSubsequences(nums []int) int {
    const MOD = 1_000_000_007
    n := len(nums)
    // dp[parity][consecutive]: number of subsequences ending with this parity and consecutive count (1 or 2)
    dp := [2][3]int{}
    for i := 0; i < n; i++ {
        p := nums[i] % 2
        newDp := [2][3]int{}
        // Start new subsequence with nums[i]
        newDp[p][1] = (newDp[p][1] + 1) % MOD
        // Extend all previous subsequences
        for last := 0; last < 2; last++ {
            for cnt := 1; cnt <= 2; cnt++ {
                val := dp[last][cnt]
                if val == 0 { continue }
                if last == p {
                    if cnt == 2 {
                        continue // would make three consecutive of the same parity
                    }
                    newDp[p][cnt+1] = (newDp[p][cnt+1] + val) % MOD
                } else {
                    newDp[p][1] = (newDp[p][1] + val) % MOD
                }
            }
        }
        // Merge newDp into dp
        for last := 0; last < 2; last++ {
            for cnt := 1; cnt <= 2; cnt++ {
                dp[last][cnt] = (dp[last][cnt] + newDp[last][cnt]) % MOD
            }
        }
    }
    res := 0
    for last := 0; last < 2; last++ {
        for cnt := 1; cnt <= 2; cnt++ {
            res = (res + dp[last][cnt]) % MOD
        }
    }
    return res
}
# @lc code=end