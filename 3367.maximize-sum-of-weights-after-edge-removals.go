#
# @lc app=leetcode id=3367 lang=golang
#
# [3367] Maximize Sum of Weights after Edge Removals
#

# @lc code=start
func maximizeSumOfWeights(edges [][]int, k int) int64 {
    // Step 1: Create an adjacency list from edges
    adjList := make(map[int][][]int)
    for _, edge := range edges {
        u, v, w := edge[0], edge[1], edge[2]
        adjList[u] = append(adjList[u], []int{v, w})
        adjList[v] = append(adjList[v], []int{u, w})
    }
    
    // Step 2: Implement DFS to control connections and maximize weight sum
    var dfs func(node int, parent int) int64
    dfs = func(node int, parent int) int64 {
        totalWeight := int64(0)
        var childWeights []int64
        for _, neighbor := range adjList[node] {
            if neighbor[0] != parent {
                weight := dfs(neighbor[0], node) + int64(neighbor[1])
                childWeights = append(childWeights, weight)
            }
        }
        sort.Slice(childWeights, func(i, j int) bool { return childWeights[i] > childWeights[j] })
        for i := 0; i < k && i < len(childWeights); i++ {
            totalWeight += childWeights[i]
        }
        return totalWeight
    }
    
    return dfs(0, -1) // Start DFS from root node 0 with no parent (-1)
}
# @lc code=end