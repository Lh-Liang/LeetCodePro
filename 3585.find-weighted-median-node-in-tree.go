#
# @lc app=leetcode id=3585 lang=golang
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
func findMedian(n int, edges [][]int, queries [][]int) []int {
    type Pair struct{to, w int}
    adj := make([][]Pair, n)
    for _, e := range edges {
        u, v, w := e[0], e[1], e[2]
        adj[u] = append(adj[u], Pair{v, w})
        adj[v] = append(adj[v], Pair{u, w})
    }

    LOG := 18
    parent := make([][]int, n)
    for i := 0; i < n; i++ {
        parent[i] = make([]int, LOG)
    }
    depth := make([]int, n)
    dist := make([]int64, n)
    upWeight := make([][]int64, n) // upWeight[i][k]: weight from i up 2^k steps
    for i := 0; i < n; i++ {
        upWeight[i] = make([]int64, LOG)
    }
    
    var dfs func(int, int, int, int64)
    dfs = func(u, p, d int, sum int64) {
        parent[u][0] = p
        depth[u] = d
        dist[u] = sum
        for _, nei := range adj[u] {
            if nei.to != p {
                upWeight[nei.to][0] = int64(nei.w)
                dfs(nei.to, u, d+1, sum+int64(nei.w))
            }
        }
    }
    dfs(0, 0, 0, 0)

    for k := 1; k < LOG; k++ {
        for i := 0; i < n; i++ {
            parent[i][k] = parent[parent[i][k-1]][k-1]
            upWeight[i][k] = upWeight[i][k-1] + upWeight[parent[i][k-1]][k-1]
        }
    }

    lca := func(u, v int) int {
        if depth[u] < depth[v] {
            u, v = v, u
        }
        for k := LOG-1; k >= 0; k-- {
            if depth[u]-(1<<k) >= depth[v] {
                u = parent[u][k]
            }
        }
        if u == v {
            return u
        }
        for k := LOG-1; k >= 0; k-- {
            if parent[u][k] != parent[v][k] {
                u = parent[u][k]
                v = parent[v][k]
            }
        }
        return parent[u][0]
    }

    // Helper: walk up from node 'from' towards 'to', accumulating weights, stop at first node where sum >= targetSum
    walk := func(from, to int, targetSum int64) (int, int64) {
        sum := int64(0)
        x := from
        for k := LOG-1; k >= 0; k-- {
            if depth[x]-(1<<k) >= depth[to] && sum+upWeight[x][k] < targetSum {
                sum += upWeight[x][k]
                x = parent[x][k]
            }
        }
        // One more step if needed
        if x != to && sum+upWeight[x][0] >= targetSum {
            sum += upWeight[x][0]
            x = parent[x][0]
        }
        return x, sum
    }

    // Helper: verify that 'cand' is first node from u to v where cumulative sum >= half
    verify := func(u, v, cand int, half int64) bool {
        // Build path from u to v
        path := []int{}
        var buildPath func(int, int)
        buildPath = func(x, par int) {
            path = append(path, x)
            if x == v {return}
            for _, nei := range adj[x] {
                if nei.to != par {
                    buildPath(nei.to, x)
                    if path[len(path)-1] == v {return}
                }
            }
            if path[len(path)-1] != v {
                path = path[:len(path)-1]
            }
        }
        buildPath(u, -1)
        sum := int64(0)
        for i := 1; i < len(path); i++ {
            for _, nei := range adj[path[i-1]] {
                if nei.to == path[i] { sum += int64(nei.w); break }
            }
            if sum >= half {
                return path[i] == cand
            }
        }
        return false
    }

    res := make([]int, len(queries))
    for idx, q := range queries {
        u, v := q[0], q[1]
        anc := lca(u, v)
        total := dist[u] + dist[v] - 2*dist[anc]
        half := (total + 1) / 2
        // Try from u to lca first
        cand1, sum1 := walk(u, anc, half)
        if verify(u, v, cand1, half) {
            res[idx] = cand1
            continue
        }
        // Try from v to lca
        cand2, sum2 := walk(v, anc, half)
        if verify(v, u, cand2, half) {
            res[idx] = cand2
            continue
        }
        // Fallback: linear scan along path
        // Build path from u to v (via lca)
        path := []int{}
        x := u
        for x != anc {
            path = append(path, x)
            x = parent[x][0]
        }
        path = append(path, anc)
        stack := []int{}
        x = v
        for x != anc {
            stack = append(stack, x)
            x = parent[x][0]
        }
        for i := len(stack)-1; i >= 0; i-- {
            path = append(path, stack[i])
        }
        sum := int64(0)
        found := anc
        for i := 1; i < len(path); i++ {
            for _, nei := range adj[path[i-1]] {
                if nei.to == path[i] { sum += int64(nei.w); break }
            }
            if sum >= half {
                found = path[i]
                break
            }
        }
        res[idx] = found
    }
    return res
}
# @lc code=end