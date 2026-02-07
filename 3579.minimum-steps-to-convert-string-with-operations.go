#
# @lc app=leetcode id=3579 lang=golang
#
# [3579] Minimum Steps to Convert String with Operations
#
# @lc code=start
func minOperations(word1 string, word2 string) int {
    n := len(word1)
    min := func(a, b int) int {
        if a < b { return a }
        return b
    }
    dp := make([]int, n+1)
    for i := range dp {
        dp[i] = 1 << 30
    }
    dp[0] = 0
    for i := 1; i <= n; i++ {
        for j := 0; j < i; j++ {
            s1 := word1[j:i]
            s2 := word2[j:i]
            ops := 0
            // If substrings are already equal, no ops needed
            if s1 == s2 {
                dp[i] = min(dp[i], dp[j])
                continue
            }
            // Try reverse
            rev := func(s string) string {
                b := []byte(s)
                for l, r := 0, len(b)-1; l < r; l, r = l+1, r-1 {
                    b[l], b[r] = b[r], b[l]
                }
                return string(b)
            }
            if rev(s1) == s2 {
                ops = 1
            } else {
                // Try swap: swap any two chars
                foundSwap := false
                b1 := []byte(s1)
                b2 := []byte(s2)
                l := len(s1)
                for x := 0; x < l && !foundSwap; x++ {
                    for y := x + 1; y < l; y++ {
                        b1[x], b1[y] = b1[y], b1[x]
                        if string(b1) == s2 {
                            foundSwap = true
                            break
                        }
                        b1[x], b1[y] = b1[y], b1[x]
                    }
                }
                if foundSwap {
                    ops = 1
                } else {
                    // Count replaces: count mismatches
                    cnt := 0
                    for k := 0; k < len(s1); k++ {
                        if s1[k] != s2[k] {
                            cnt++
                        }
                    }
                    ops = cnt
                }
            }
            dp[i] = min(dp[i], dp[j]+ops)
        }
    }
    return dp[n]
}
# @lc code=end