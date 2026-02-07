#
# @lc app=leetcode id=3786 lang=golang
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
func interactionCosts(n int, edges [][]int, group []int) int64 {
    // Create an adjacency list from edges.
    adjList := make([][]int, n)
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        adjList[u] = append(adjList[u], v)
        adjList[v] = append(adjList[v], u)
    }

    // Precompute the size of subtrees using DFS.
    subtreeSizes := make([]int, n)
    visited := make([]bool, n)
    var dfs func(node int) int
    dfs = func(node int) int {
        visited[node] = true
        size := 1 // Start with counting the node itself
        for _, neighbor := range adjList[node] {
            if !visited[neighbor] {
                size += dfs(neighbor)
            }
        }
        subtreeSizes[node] = size
        return size
    }
    dfs(0) // Start DFS from node 0 (or any arbitrary root node as it's a tree)

    // Map groups to their respective nodes.
    groupMap := make(map[int][]int)
    for i := 0; i < n; i++ {
        groupMap[group[i]] = append(groupMap[group[i]], i)
    }

    totalCost := int64(0)

    // Calculate the total interaction cost within each group.
    for _, nodes := range groupMap {
        if len(nodes) > 1 { // Only consider groups with more than one node.
            for _, startNode := range nodes {
                visited = make([]bool, n) // Reset visited array for new DFS traversal
                var dfsCost func(node int, parent int) int64
                dfsCost = func(node int, parent int) int64 {
                    visited[node] = true
                    cost := int64(0)
                    for _, neighbor := range adjList[node] {
                        if neighbor != parent && group[neighbor] == group[node] && !visited[neighbor] {
                            cost += dfsCost(neighbor, node) + 1 // Add distance contribution from this edge
                        }
                    }
                    return cost + int64(subtreeSizes[node]-1) // Add contribution from all descendants in this subtree
                }
                totalCost += dfsCost(startNode, -1)
            }
            totalCost /= 2 // Each pair is counted twice in undirected graphs, so divide by two.
        }
    }

    return totalCost
}
# @lc code=end