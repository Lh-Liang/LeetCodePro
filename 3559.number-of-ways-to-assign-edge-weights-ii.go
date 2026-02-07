#
# @lc app=leetcode id=3559 lang=golang
#
# [3559] Number of Ways to Assign Edge Weights II
#

# @lc code=start
func assignEdgeWeights(edges [][]int, queries [][]int) []int {
    const MOD = int(1e9 + 7)
    n := len(edges) + 1
    tree := make([][]int, n+1)
    for _, e := range edges {
        u, v := e[0], e[1]
        tree[u] = append(tree[u], v)
        tree[v] = append(tree[v], u)
    }
    LOG := 20
    depth := make([]int, n+1)
    parent := make([][]int, n+1)
    for i := range parent {
        parent[i] = make([]int, LOG)
    }
    var dfs func(int, int)
    dfs = func(u, p int) {
        parent[u][0] = p
        for i := 1; i < LOG; i++ {
            parent[u][i] = parent[parent[u][i-1]][i-1]
        }
        for _, v := range tree[u] {
            if v != p {
                depth[v] = depth[u] + 1
                dfs(v, u)
            }
        }
    }
    dfs(1, 0)
    lca := func(u, v int) int {
        // Bring u and v to the same depth
        if depth[u] < depth[v] {
            u, v = v, u
        }
        for i := LOG - 1; i >= 0; i-- {
            if depth[parent[u][i]] >= depth[v] {
                u = parent[u][i]
            }
        }
        if u == v {
            return u
        }
        for i := LOG - 1; i >= 0; i-- {
            if parent[u][i] != parent[v][i] {
                u = parent[u][i]
                v = parent[v][i]
            }
        }
        return parent[u][0]
    }
    // Precompute powers of 2 modulo MOD
    pow2 := make([]int, n+2)
    pow2[0] = 1
    for i := 1; i < len(pow2); i++ {
        pow2[i] = (pow2[i-1] * 2) % MOD
    }
    res := make([]int, len(queries))
    for i, q := range queries {
        u, v := q[0], q[1]
        if u == v {
            // Path with zero edges cannot have odd total cost
            res[i] = 0
            continue
        }
        anc := lca(u, v)
        k := depth[u] + depth[v] - 2*depth[anc] // Number of edges in path
        // By combinatorial analysis, number of assignments with odd sum is 2^{k-1} for k >= 1
        ans := pow2[k-1]
        // Sanity check: For k == 0, ans must be 0
        if k == 0 {
            ans = 0
        }
        res[i] = ans
    }
    return res
}
# @lc code=end