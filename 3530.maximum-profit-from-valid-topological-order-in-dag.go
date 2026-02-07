#
# @lc app=leetcode id=3530 lang=golang
#
# [3530] Maximum Profit from Valid Topological Order in DAG
#

# @lc code=start
func maxProfit(n int, edges [][]int, score []int) int {
    // Create adjacency list and indegree count for Kahn's algorithm
    adj := make([][]int, n)
    indegree := make([]int, n)
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        adj[u] = append(adj[u], v)
        indegree[v]++
    }
    
    // Initialize queue with all nodes having zero indegree (no dependencies)
    queue := []int{}
    for i := 0; i < n; i++ {
        if indegree[i] == 0 {
            queue = append(queue, i)
        }
    }
    
    // Perform Kahn's algorithm for topological sorting
    topoOrder := []int{}
    for len(queue) > 0 {
        node := queue[0]
        queue = queue[1:]
        topoOrder = append(topoOrder, node)
        for _, neighbor := range adj[node] {
            indegree[neighbor]--
            if indegree[neighbor] == 0 {
                queue = append(queue, neighbor)
            }
        }
    }
    
    // Calculate maximum profit using scores and topological order position
    maxProfit := 0
    dp := make([][]int, n+1)
    for i := range dp {
        dp[i] = make([]int, n+1)
    }

    // Using dynamic programming to maximize profit respecting topological constraints
    for pos := 1; pos <= n; pos++ {
        for _, node := range topoOrder {
            dp[pos][node] = score[node]*pos + dp[pos-1][node]
            maxProfit = max(maxProfit, dp[pos][node])
        }
    }

    return maxProfit
}
nfunc max(x, y int) int { if x > y { return x } else { return y } }
n# @lc code=end