#
# @lc app=leetcode id=3425 lang=golang
#
# [3425] Longest Special Path
#

# @lc code=start
func longestSpecialPath(edges [][]int, nums []int) []int {
    n := len(nums)
    adj := make([][][2]int, n)
    for _, e := range edges {
        u, v, w := e[0], e[1], e[2]
        adj[u] = append(adj[u], [2]int{v, w})
        adj[v] = append(adj[v], [2]int{u, w})
    }
    maxLen := 0
    minNodes := n+1
    var dfs func(u, parent int, seen map[int]struct{}, curLen, curNodes int)
    dfs = func(u, parent int, seen map[int]struct{}, curLen, curNodes int) {
        if _, exists := seen[nums[u]]; exists {
            if curLen > maxLen {
                maxLen = curLen
                minNodes = curNodes
            } else if curLen == maxLen && curNodes < minNodes {
                minNodes = curNodes
            }
            return
        }
        seen[nums[u]] = struct{}{}
        extended := false
        for _, pair := range adj[u] {
            v, w := pair[0], pair[1]
            if v == parent { continue }
            extended = true
            dfs(v, u, seen, curLen + w, curNodes + 1)
        }
        if !extended {
            if curLen > maxLen {
                maxLen = curLen
                minNodes = curNodes
            } else if curLen == maxLen && curNodes < minNodes {
                minNodes = curNodes
            }
        }
        delete(seen, nums[u])
    }
    dfs(0, -1, make(map[int]struct{}), 0, 1)
    return []int{maxLen, minNodes}
}
# @lc code=end