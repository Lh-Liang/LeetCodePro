#
# @lc app=leetcode id=3553 lang=golang
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#
# @lc code=start
func minimumWeight(edges [][]int, queries [][]int) []int {
    n := len(edges) + 1
    tree := make([][][2]int, n)
    for _, e := range edges {
        u, v, w := e[0], e[1], e[2]
        tree[u] = append(tree[u], [2]int{v, w})
        tree[v] = append(tree[v], [2]int{u, w})
    }
    const LOG = 17 // since n <= 1e5, log2(1e5) < 17
    parent := make([][]int, n)
    up := make([][]int, n)
    depth := make([]int, n)
    sum := make([]int, n)
    for i := range parent {
        parent[i] = make([]int, LOG)
        up[i] = make([]int, LOG)
        for j := 0; j < LOG; j++ {
            parent[i][j] = -1
        }
    }
    var dfs func(u, p, d, s int)
    dfs = func(u, p, d, s int) {
        parent[u][0] = p
        depth[u] = d
        sum[u] = s
        for _, e := range tree[u] {
            v, w := e[0], e[1]
            if v != p {
                dfs(v, u, d+1, s+w)
            }
        }
    }
    dfs(0, -1, 0, 0)
    for j := 1; j < LOG; j++ {
        for i := 0; i < n; i++ {
            if parent[i][j-1] != -1 {
                parent[i][j] = parent[parent[i][j-1]][j-1]
            }
        }
    }
    lca := func(u, v int) int {
        if depth[u] < depth[v] {
            u, v = v, u
        }
        for k := LOG-1; k >= 0; k-- {
            if parent[u][k] != -1 && depth[parent[u][k]] >= depth[v] {
                u = parent[u][k]
            }
        }
        if u == v {
            return u
        }
        for k := LOG-1; k >= 0; k-- {
            if parent[u][k] != -1 && parent[u][k] != parent[v][k] {
                u = parent[u][k]
                v = parent[v][k]
            }
        }
        return parent[u][0]
    }
    minSubtreeLCA := func(a, b, c int) int {
        x := lca(a, b)
        y := lca(b, c)
        z := lca(a, c)
        // The LCA of all three nodes is the 'lowest' one among x, y, z
        // Since tree, they are on the same path
        if depth[x] < depth[y] {
            x = y
        }
        if depth[x] < depth[z] {
            x = z
        }
        return x
    }
    ans := make([]int, len(queries))
    for i, q := range queries {
        a, b, c := q[0], q[1], q[2]
        u := minSubtreeLCA(a, b, c)
        total := sum[a] + sum[b] + sum[c] - 2*sum[u]
        // Additional check (domain-agnostic): ensure that all nodes are distinct and subtree covers all required nodes
        // This is always true by construction in a tree, but would be checked if generalizing
        ans[i] = total
    }
    return ans
}
# @lc code=end