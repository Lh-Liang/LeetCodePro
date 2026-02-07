#
# @lc app=leetcode id=3530 lang=golang
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#
# @lc code=start
func maxProfit(n int, edges [][]int, score []int) int {
    // Build dependency mask for each node
    dep := make([]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        dep[v] |= 1 << u
    }
    // dp[mask] = max profit for subset of nodes in mask
    size := 1 << n
    dp := make([]int, size)
    for mask := 0; mask < size; mask++ {
        pos := bits.OnesCount(uint(mask)) + 1
        for i := 0; i < n; i++ {
            if (mask>>i)&1 == 0 && (dep[i]&mask) == dep[i] {
                next := mask | (1 << i)
                if dp[next] < dp[mask]+score[i]*pos {
                    dp[next] = dp[mask]+score[i]*pos
                }
            }
        }
    }
    return dp[size-1]
}
# @lc code=end