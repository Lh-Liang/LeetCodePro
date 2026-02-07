#
# @lc app=leetcode id=3419 lang=golang
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
func minMaxWeight(n int, edges [][]int, threshold int) int {
    canReach := func(maxWeight int) bool {
        out := make([][]struct{to, w int}, n)
        for _, e := range edges {
            a, b, w := e[0], e[1], e[2]
            if w <= maxWeight {
                out[a] = append(out[a], struct{to, w int}{b, w})
            }
        }
        for i := 0; i < n; i++ {
            sort.Slice(out[i], func(a, b int) bool {
                return out[i][a].w < out[i][b].w
            })
            if len(out[i]) > threshold {
                out[i] = out[i][:threshold]
            }
        }
        // Ensure all nodes have at most threshold outgoing edges (enforced above)
        // Now check reachability
        rev := make([][]int, n)
        for from, ls := range out {
            for _, e := range ls {
                rev[e.to] = append(rev[e.to], from)
            }
        }
        visited := make([]bool, n)
        queue := []int{0}
        visited[0] = true
        for len(queue) > 0 {
            node := queue[0]
            queue = queue[1:]
            for _, nb := range rev[node] {
                if !visited[nb] {
                    visited[nb] = true
                    queue = append(queue, nb)
                }
            }
        }
        for i := 0; i < n; i++ {
            if !visited[i] {
                return false
            }
        }
        // All constraints are satisfied
        return true
    }
    left, right := 1, 1_000_000
    ans := -1
    for left <= right {
        mid := (left + right) / 2
        if canReach(mid) {
            ans = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return ans
}
# @lc code=end