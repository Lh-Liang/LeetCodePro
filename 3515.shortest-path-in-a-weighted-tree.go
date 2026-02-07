#
# @lc app=leetcode id=3515 lang=golang
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
func treeQueries(n int, edges [][]int, queries [][]int) []int {
    // Step 1: Build adjacency list representation of tree
    adjList := make(map[int][][2]int) // node -> [(neighbor, weight)]
    for _, edge := range edges {
        u, v, w := edge[0], edge[1], edge[2]
        adjList[u] = append(adjList[u], [2]int{v, w})
        adjList[v] = append(adjList[v], [2]int{u, w})
    }
    
    // Step 2: Initialize variables for DFS and results storage
    distance := make(map[int]int)
    visited := make(map[int]bool)
    var dfs func(node, currentDistance int)
    dfs = func(node, currentDistance int) {
        visited[node] = true
        distance[node] = currentDistance
        for _, neighbor := range adjList[node] {
            if !visited[neighbor[0]] {
                dfs(neighbor[0], currentDistance + neighbor[1])
            }
        }
    }
    
    // Step 3: Process each query based on its type (update or path calculation)
    result := []int{}\\\\\\\\
n   	for _, query := range queries {\\\\\\nn   		if query[0] == 1 { // Update query [1, u, v, w']}            u, v, newWeight := query[1], query[2], query[3]}            // Update adjacency list with new weight}            for i := range adjList[u] {                if adjList[u][i][0] == v {                    adjList[u][i][1] = newWeight}                    break}}            }            for i := range adjList[v] {                if adjList[v][i][0] == u {                    adjList[v][i][1] = newWeight}                    break}}            }}        } else if query[0] == 2 { // Path calculation query [2, x]            x := query[1]            visited = map[int]bool{}            dfs(1, 0)            result = append(result, distance[x])}}n   	}n   	return resultn}