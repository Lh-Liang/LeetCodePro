#
# @lc app=leetcode id=3441 lang=golang
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
func minCostGoodCaption(caption string) string {
    n := len(caption)
    if n < 3 {
        return ""
    }
    INF := 1<<30
    type State struct {
        cost int
        str  string
    }
    dp := make([]State, n+1)
    for i := range dp {
        dp[i] = State{INF, ""}
    }
    dp[0] = State{0, ""}
    // Precompute cumulative costs for each character
    cum := make([][]int, 26)
    for ch := 0; ch < 26; ch++ {
        cum[ch] = make([]int, n+1)
        for i := 1; i <= n; i++ {
            diff := abs(int(caption[i-1])-('a'+ch)) // Each operation is a single step between neighbors
            cum[ch][i] = cum[ch][i-1] + diff
        }
    }
    for i := 3; i <= n; i++ {
        for j := i - 3; j >= 0; j-- {
            length := i - j
            if length < 3 {
                break
            }
            for ch := 0; ch < 26; ch++ {
                cost := cum[ch][i] - cum[ch][j]
                prev := dp[j]
                newCost := prev.cost + cost
                block := make([]byte, length)
                for k := 0; k < length; k++ {
                    block[k] = byte('a' + ch)
                }
                candidate := prev.str + string(block)
                if newCost < dp[i].cost || (newCost == dp[i].cost && candidate < dp[i].str) {
                    dp[i] = State{newCost, candidate}
                }
            }
        }
    }
    if dp[n].cost >= INF {
        return ""
    }
    // Final verification: check all blocks are at least length 3
    s := dp[n].str
    cnt := 1
    for i := 1; i < n; i++ {
        if s[i] == s[i-1] {
            cnt++
        } else {
            if cnt < 3 {
                return ""
            }
            cnt = 1
        }
    }
    if cnt < 3 {
        return ""
    }
    return s
}
func abs(x int) int { if x < 0 { return -x }; return x }
# @lc code=end