#
# @lc app=leetcode id=3544 lang=golang
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
func subtreeInversionSum(edges [][]int, nums []int, k int) int64 {
    n := len(nums)
    adj := make([][]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }
    type state struct{ node, dist int }
    memo := make(map[state]int64)
    var dfs func(u, parent, dist int) int64
    dfs = func(u, parent, dist int) int64 {
        key := state{u, dist}
        if val, ok := memo[key]; ok {
            return val
        }
        // Case 1: do not invert at u
        sum0 := int64(nums[u])
        for _, v := range adj[u] {
            if v == parent { continue }
            sum0 += dfs(v, u, min(dist+1, k))
        }
        res := sum0
        // Case 2: invert at u if allowed
        if dist >= k {
            sum1 := int64(-nums[u])
            for _, v := range adj[u] {
                if v == parent { continue }
                sum1 += dfs(v, u, 1)
            }
            if sum1 > res {
                res = sum1
            }
        }
        memo[key] = res
        return res
    }
    return dfs(0, -1, k)
}
# @lc code=end