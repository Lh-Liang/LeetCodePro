# @lc app=leetcode id=3585 lang=golang
#
# [3585] Find Weighted Median Node in Tree
#
# @lc code=start
func findMedian(n int, edges [][]int, queries [][]int) []int {
    // Step 1: Create adjacency list representation of tree.
    adj := make(map[int]map[int]int)
    for _, edge := range edges {
        u, v, w := edge[0], edge[1], edge[2]
        if _, exists := adj[u]; !exists {
            adj[u] = make(map[int]int)
        }
        if _, exists := adj[v]; !exists {
            adj[v] = make(map[int]int)
        }
        adj[u][v] = w
        adj[v][u] = w
    }
    
    // Helper function to find weighted median node for a single query.
    var findWeightedMedian func(start, end int) int
    findWeightedMedian = func(start, end int) int {
        stack := []int{start}
        visited := make([]bool, n)
        parent := make([]int, n)
        weights := make([]int, n)
        visited[start] = true
        parent[start] = -1
        for len(stack) > 0 {
            node := stack[len(stack)-1]
            stack = stack[:len(stack)-1]
            if node == end {
                break
            }
            for neighbor, weight := range adj[node] {
                if !visited[neighbor] {
                    visited[neighbor] = true
                    parent[neighbor] = node
                    weights[neighbor] = weight
                    stack = append(stack, neighbor)
                }
            }
        }
        
        // Calculate total weight of path from start to end.
        totalWeight := 0
        pathNode := end
        for parent[pathNode] != -1 {
            totalWeight += weights[pathNode]
            pathNode = parent[pathNode]
        }
       	// Find weighted median node along path.						halfWeight := totalWeight / 2 
cumulativeWeightSum := 0 
currNode:= end 	for currNode != start {
cumulativeWeightSum += weights[currNode]	if cumulativeWeightSum >= halfWeight {return currNode}currNode= parent[currNode]}return start}	// Process each query and store results in ans slice.	ans:= make([]int,len(queries))	for i,q:= range queries {	ans[i]=findWeightedMedian(q[0], q[1])}	return ans}	# @lc code=end