#
# @lc app=leetcode id=3310 lang=golang
#
# [3310] Remove Methods From Project
#

# @lc code=start
func remainingMethods(n int, k int, invocations [][]int) []int {
    // Create adjacency lists for the graph representation
    adjList := make([][]int, n)
    reverseAdjList := make([][]int, n)
    for _, invocation := range invocations {
        adjList[invocation[0]] = append(adjList[invocation[0]], invocation[1])
        reverseAdjList[invocation[1]] = append(reverseAdjList[invocation[1]], invocation[0])
    }
    
    // Find all suspicious methods using DFS starting from method k
    suspicious := make([]bool, n)
    var dfs func(node int)
    dfs = func(node int) {
        if suspicious[node] {
            return
        }
        suspicious[node] = true
        for _, nei := range adjList[node] {
            dfs(nei)
        }
    }
    dfs(k)
    
    // Check for any incoming edges to the suspicious set from outside
    canRemoveSuspicious := true
    for i := 0; i < n; i++ {
        if !suspicious[i] { // Only consider non-suspicious methods
            for _, nei := range adjList[i] {
                if suspicious[nei] { // Found an incoming edge to a suspicious method
                    canRemoveSuspicious = false
                    break
                }
            }
        }
        if !canRemoveSuspicious {
            break
        }
    }
    
    // Determine result based on whether we can safely remove suspicious methods or not
    result := []int{}
    if canRemoveSuspicious {
        for i := 0; i < n; i++ {
            if !suspicious[i] {
                result = append(result, i)
            }
        }
    } else {
        for i := 0; i < n; i++ {
            result = append(result, i)
        }
    }
    return result
}
# @lc code=end