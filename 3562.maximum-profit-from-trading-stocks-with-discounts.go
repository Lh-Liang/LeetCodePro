#
# @lc app=leetcode id=3562 lang=golang
#
# [3562] Maximum Profit from Trading Stocks with Discounts
#
# @lc code=start
import (
    "math"
)

func maxProfit(n int, present []int, future []int, hierarchy [][]int, budget int) int {
    tree := make([][]int, n)
    for _, edge := range hierarchy {
        u, v := edge[0]-1, edge[1]-1
        tree[u] = append(tree[u], v)
    }

    // Knapsack merge helper: merges two DP arrays under budget constraint
    mergeDP := func(dp1, dp2 []int) []int {
        res := make([]int, budget+1)
        for i := 0; i <= budget; i++ {
            res[i] = math.MinInt32
        }
        for c1 := 0; c1 <= budget; c1++ {
            if dp1[c1] == math.MinInt32 { continue }
            for c2 := 0; c2 <= budget-c1; c2++ {
                if dp2[c2] == math.MinInt32 { continue }
                if dp1[c1]+dp2[c2] > res[c1+c2] {
                    res[c1+c2] = dp1[c1]+dp2[c2]
                }
            }
        }
        return res
    }

    var dfs func(node int, bossBought bool) []int
    dfs = func(node int, bossBought bool) []int {
        // DP array: dp[cost] = max profit with total cost 'cost'
        dp := make([]int, budget+1)
        for i := range dp {
            dp[i] = math.MinInt32
        }
        dp[0] = 0
        // Case 1: Not buying this stock, merge all children's DPs in not-buying mode
        for _, child := range tree[node] {
            childDp := dfs(child, false)
            dp = mergeDP(dp, childDp)
        }
        res := make([]int, budget+1)
        copy(res, dp)
        // Case 2: Buying this stock
        buyPrice := present[node]
        if bossBought {
            buyPrice = present[node] / 2
        }
        if buyPrice <= budget {
            buyProfit := future[node] - buyPrice
            dp2 := make([]int, budget+1)
            for i := range dp2 {
                dp2[i] = math.MinInt32
            }
            dp2[buyPrice] = buyProfit
            for _, child := range tree[node] {
                childDp := dfs(child, true)
                dp2 = mergeDP(dp2, childDp)
            }
            // Merge: select maximum profit for each cost
            for c := 0; c <= budget; c++ {
                if dp2[c] > res[c] {
                    res[c] = dp2[c]
                }
            }
        }
        // Verification (optional): ensure all res[c] <= budget and not MinInt32 unless achievable
        return res
    }
    ans := dfs(0, false)
    maxP := 0
    for c := 0; c <= budget; c++ {
        if ans[c] > maxP {
            maxP = ans[c]
        }
    }
    return maxP
}
# @lc code=end