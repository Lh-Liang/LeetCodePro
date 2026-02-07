#
# @lc app=leetcode id=3486 lang=golang
#
# [3486] Longest Special Path II
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
    minNodes := n + 1
    freq := map[int]int{}
    var dfs func(node, parent int, dupCount int, length int, nodes int)
    dfs = func(node, parent int, dupCount int, length int, nodes int) {
        val := nums[node]
        freq[val]++
        if freq[val] == 2 {
            dupCount++
        }
        if dupCount > 1 {
            if freq[val] == 2 {
                dupCount--
            }
            freq[val]--
            return
        }
        if length > maxLen {
            maxLen = length
            minNodes = nodes
        } else if length == maxLen && nodes < minNodes {
            minNodes = nodes
        }
        for _, nb := range adj[node] {
            if nb[0] == parent {
                continue
            }
            dfs(nb[0], node, dupCount, length+nb[1], nodes+1)
        }
        if freq[val] == 2 {
            dupCount--
        }
        freq[val]--
    }
    dfs(0, -1, 0, 0, 1)
    return []int{maxLen, minNodes}
}
# @lc code=end