#
# @lc app=leetcode id=3310 lang=golang
#
# [3310] Remove Methods From Project
#
# @lc code=start
func remainingMethods(n int, k int, invocations [][]int) []int {
    // Step 1: Build adjacency list
    adj := make([][]int, n)
    for _, inv := range invocations {
        from, to := inv[0], inv[1]
        adj[from] = append(adj[from], to)
    }
    // Step 2: Find suspicious set via BFS from k
    suspicious := make([]bool, n)
    queue := []int{k}
    suspicious[k] = true
    for len(queue) > 0 {
        curr := queue[0]
        queue = queue[1:]
        for _, nei := range adj[curr] {
            if !suspicious[nei] {
                suspicious[nei] = true
                queue = append(queue, nei)
            }
        }
    }
    // Step 3: Check for outside invocations into suspicious set
    for _, inv := range invocations {
        from, to := inv[0], inv[1]
        if !suspicious[from] && suspicious[to] {
            res := make([]int, n)
            for i := 0; i < n; i++ {
                res[i] = i
            }
            return res
        }
    }
    // Step 4: Return all methods not in suspicious set
    var res []int
    for i := 0; i < n; i++ {
        if !suspicious[i] {
            res = append(res, i)
        }
    }
    return res
}
# @lc code=end