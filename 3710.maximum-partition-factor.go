#
# @lc app=leetcode id=3710 lang=golang
#
# [3710] Maximum Partition Factor
#

# @lc code=start
func maxPartitionFactor(points [][]int) int {
    n := len(points)
    if n == 2 {
        return 0
    }
    // Manhattan distance function
    manhattan := func(i, j int) int {
        dx := points[i][0] - points[j][0]
        if dx < 0 { dx = -dx }
        dy := points[i][1] - points[j][1]
        if dy < 0 { dy = -dy }
        return dx + dy
    }
    // Precompute all pairwise distances
    pairs := make([]struct{ i, j, d int }, 0, n*n)
    for i := 0; i < n; i++ {
        for j := i+1; j < n; j++ {
            pairs = append(pairs, struct{ i, j, d int }{i, j, manhattan(i, j)})
        }
    }
    // Binary search for the answer
    left, right := 1, int(2e8)
    ans := 0
    for left <= right {
        mid := (left + right) / 2
        // Build the graph: connect points with distance < mid
        parent := make([]int, n)
        for i := 0; i < n; i++ { parent[i] = i }
        var find func(int) int
        find = func(x int) int {
            if parent[x] != x {
                parent[x] = find(parent[x])
            }
            return parent[x]
        }
        union := func(x, y int) {
            px, py := find(x), find(y)
            if px != py { parent[px] = py }
        }
        for _, p := range pairs {
            if p.d < mid {
                union(p.i, p.j)
            }
        }
        compMap := make(map[int][]int)
        for i := 0; i < n; i++ {
            root := find(i)
            compMap[root] = append(compMap[root], i)
        }
        comps := make([][]int, 0, len(compMap))
        for _, v := range compMap {
            comps = append(comps, v)
        }
        m := len(comps)
        found := false
        // Try all non-trivial bipartitions of components
        for mask := 1; mask < (1<<m)-1; mask++ {
            cntA, cntB := 0, 0
            for i := 0; i < m; i++ {
                if (mask>>i)&1 == 1 {
                    cntA += len(comps[i])
                } else {
                    cntB += len(comps[i])
                }
            }
            if cntA > 0 && cntB > 0 {
                found = true
                break
            }
        }
        if found {
            ans = mid
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return ans
}
# @lc code=end