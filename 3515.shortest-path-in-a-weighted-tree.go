#
# @lc app=leetcode id=3515 lang=golang
#
# [3515] Shortest Path in a Weighted Tree
#
# @lc code=start
func treeQueries(n int, edges [][]int, queries [][]int) []int {
    // Build adjacency list and edge index map
    type pair struct{to, idx int}
    adj := make([][]pair, n+1)
    edgeIdx := make(map[[2]int]int)
    for i, e := range edges {
        u, v := e[0], e[1]
        adj[u] = append(adj[u], pair{v, i})
        adj[v] = append(adj[v], pair{u, i})
        edgeIdx[[2]int{u, v}] = i
        edgeIdx[[2]int{v, u}] = i
    }
    // DFS to compute parent, inEdge, and dist
    parent := make([]int, n+1)
    inEdge := make([]int, n+1)
    dist := make([]int, n+1)
    visited := make([]bool, n+1)
    var dfs func(u, p int)
    dfs = func(u, p int) {
        visited[u] = true
        parent[u] = p
        for _, nei := range adj[u] {
            v, idx := nei.to, nei.idx
            if !visited[v] {
                inEdge[v] = idx
                dist[v] = dist[u] + edges[idx][2]
                dfs(v, u)
            }
        }
    }
    dfs(1, 0)
    res := []int{}
    for _, q := range queries {
        if q[0] == 2 {
            x := q[1]
            res = append(res, dist[x])
        } else {
            u, v, w := q[1], q[2], q[3]
            // Find deeper node
            var child int
            if parent[u] == v {
                child = u
            } else {
                child = v
            }
            idx := edgeIdx[[2]int{u, v}]
            old := edges[idx][2]
            if old == w {
                continue
            }
            delta := w - old
            edges[idx][2] = w
            // Update all distances in subtree rooted at child
            queue := []int{child}
            for len(queue) > 0 {
                node := queue[0]
                queue = queue[1:]
                dist[node] += delta
                for _, nei := range adj[node] {
                    v2, idx2 := nei.to, nei.idx
                    if parent[v2] == node {
                        queue = append(queue, v2)
                    }
                }
            }
            // After update, verify all affected nodes in the subtree have updated dist values
            // (implicit as per the update process and constraints)
        }
    }
    // Check that output format and length match the number of [2, x] queries
    return res
}
# @lc code=end