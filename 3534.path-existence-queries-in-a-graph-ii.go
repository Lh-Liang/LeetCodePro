#
# @lc app=leetcode id=3534 lang=golang
#
# [3534] Path Existence Queries in a Graph II
#
# @lc code=start
func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []int {
    type pair struct{idx, val int}
    parent := make([]int, n)
    for i := range parent { parent[i] = i }
    var find func(int) int
    find = func(x int) int {
        if parent[x] != x {
            parent[x] = find(parent[x])
        }
        return parent[x]
    }
    union := func(x, y int) {
        fx, fy := find(x), find(y)
        if fx != fy { parent[fx] = fy }
    }
    // Build adjacency list: for every pair within maxDiff, add edge
    idxs := make([]pair, n)
    for i, v := range nums {
        idxs[i] = pair{i, v}
    }
    sort.Slice(idxs, func(i, j int) bool { return idxs[i].val < idxs[j].val })
    adj := make([][]int, n)
    // For each node, scan forward and backward for all neighbors within maxDiff
    for i := 0; i < n; i++ {
        for j := i+1; j < n && idxs[j].val-idxs[i].val <= maxDiff; j++ {
            adj[idxs[i].idx] = append(adj[idxs[i].idx], idxs[j].idx)
            adj[idxs[j].idx] = append(adj[idxs[j].idx], idxs[i].idx)
            union(idxs[i].idx, idxs[j].idx)
        }
    }
    res := make([]int, len(queries))
    group := map[int][]int{}
    for i, q := range queries {
        if find(q[0]) != find(q[1]) {
            res[i] = -1
        } else if q[0] == q[1] {
            res[i] = 0
        } else {
            group[q[0]] = append(group[q[0]], i)
        }
    }
    vis := make([]int, n)
    stamp := 1
    for u, idxs := range group {
        queue := []int{u}
        dist := make([]int, n)
        for i := 0; i < n; i++ { dist[i] = -1 }
        dist[u] = 0
        vis[u] = stamp
        head := 0
        for head < len(queue) {
            v := queue[head]
            head++
            for _, w := range adj[v] {
                if vis[w] != stamp {
                    vis[w] = stamp
                    dist[w] = dist[v] + 1
                    queue = append(queue, w)
                }
            }
        }
        for _, idx := range idxs {
            v := queries[idx][1]
            res[idx] = dist[v]
        }
        stamp++
    }
    return res
}
# @lc code=end