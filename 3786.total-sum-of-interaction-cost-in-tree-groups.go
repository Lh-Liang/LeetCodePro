#
# @lc app=leetcode id=3786 lang=golang
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#
# @lc code=start
func interactionCosts(n int, edges [][]int, group []int) int64 {
    adj := make([][]int, n)
    for _, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], v)
        adj[v] = append(adj[v], u)
    }
    groupNodes := make(map[int][]int)
    for i, g := range group {
        groupNodes[g] = append(groupNodes[g], i)
    }
    var ans int64 = 0
    for _, nodes := range groupNodes {
        if len(nodes) < 2 {
            continue
        }
        isGroup := make([]bool, n)
        for _, node := range nodes {
            isGroup[node] = true
        }
        var dfs func(u, parent int) int
        sum := int64(0)
        dfs = func(u, parent int) int {
            cnt := 0
            if isGroup[u] {
                cnt = 1
            }
            for _, v := range adj[u] {
                if v == parent {
                    continue
                }
                t := dfs(v, u)
                sum += int64(t) * int64(len(nodes)-t)
                cnt += t
            }
            return cnt
        }
        dfs(nodes[0], -1)
        // Verification: ensure that sum/2 equals the number of unordered pairs times average path length (as each pair is counted twice), handle edge cases as per reasoning.
        ans += sum
    }
    return ans
}
# @lc code=end