#
# @lc app=leetcode id=3493 lang=golang
#
# [3493] Properties Graph
#

# @lc code=start
func numberOfComponents(properties [][]int, k int) int {
    n := len(properties)
    // Preprocess: Convert each properties[i] to a set for fast intersection
    sets := make([]map[int]struct{}, n)
    for i := 0; i < n; i++ {
        sets[i] = make(map[int]struct{})
        for _, v := range properties[i] {
            sets[i][v] = struct{}{}
        }
    }
    // Build adjacency list
    adj := make([][]int, n)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            count := 0
            for v := range sets[i] {
                if _, ok := sets[j][v]; ok {
                    count++
                }
            }
            if count >= k {
                adj[i] = append(adj[i], j)
                adj[j] = append(adj[j], i)
            }
        }
    }
    // DFS to count connected components
    visited := make([]bool, n)
    var dfs func(int)
    dfs = func(u int) {
        visited[u] = true
        for _, v := range adj[u] {
            if !visited[v] {
                dfs(v)
            }
        }
    }
    count := 0
    for i := 0; i < n; i++ {
        if !visited[i] {
            dfs(i)
            count++
        }
    }
    return count
}
# @lc code=end