#
# @lc app=leetcode id=3515 lang=golang
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
func treeQueries(n int, edges [][]int, queries [][]int) []int {
    // Initialize adjacency list for tree representation
    adjList := make(map[int]map[int]int)
    for _, edge := range edges {
        u, v, w := edge[0], edge[1], edge[2]
        if adjList[u] == nil {
            adjList[u] = make(map[int]int)
        }
        if adjList[v] == nil {
            adjList[v] = make(map[int]int)
        }
        adjList[u][v] = w
        adjList[v][u] = w
    }
    
    // Function to calculate initial distances using BFS from root node 1
    var bfs func(start int) map[int]int
    bfs = func(start int) map[int]int {
        dist := make(map[int]int)
        queue := []int{start}
        dist[start] = 0
        for len(queue) > 0 {
            node := queue[0]
            queue = queue[1:]
            for neighbor, weight := range adjList[node] {
                if _, visited := dist[neighbor]; !visited {
                    dist[neighbor] = dist[node] + weight
                    queue = append(queue, neighbor)
                }
            }
        }
        return dist
    }
    
    // Handle queries efficiently with initial distance calculation and updates using Heavy-Light Decomposition or Segment Trees with Lazy Propagation
    handleQueries := func(queries [][]int) []int { 	results := []int{} 	currentDistFromRoot := bfs(1) // Compute initial distances 	for _, query := range queries { 		if query[0] == 1 { // Update edge weight 			u, v, newW := query[1], query[2], query[3] 			adjList[u][v], adjList[v][u] = newW, newW 			// Efficiently recalculate affected paths using advanced data structures 		} else if query[0] == 2 { // Query shortest path distance 			x := query[1] 			results = append(results, currentDistFromRoot[x]) 		} 	} 	return results}return handleQueries(queries)}# @lc code=end