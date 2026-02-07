#
# @lc app=leetcode id=3504 lang=golang
#
# [3504] Longest Palindrome After Substring Concatenation II
#

# @lc code=start
func longestPalindrome(s string, t string) int {
    n := len(s)
    m := len(t)
    // dp[i][j] will store the length of longest palindromic subsequence
    // within s[0:i] + t[0:j]
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, m+1)
    }
    // Fill DP table considering all substrings of s and t
    for i := 0; i <= n; i++ {
        for j := 0; j <= m; j++ {
            if i > 0 {
                dp[i][j] = max(dp[i][j], dp[i-1][j])
            }
            if j > 0 {
                dp[i][j] = max(dp[i][j], dp[i][j-1])
            }
            if i > 0 && j > 0 && s[i-1] == t[j-1] {
                dp[i][j] = max(dp[i][j], dp[i-1][j-1] + 2) // Add two for mirrored characters
            }
        }
    }
    return dp[n][m]
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
# @lc code=end