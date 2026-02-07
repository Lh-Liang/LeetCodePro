#
# @lc app=leetcode id=3534 lang=golang
#
# [3534] Path Existence Queries in a Graph II
#

# @lc code=start
func pathExistenceQueries(n int, nums []int, maxDiff int, queries [][]int) []int {
    // Create adjacency list based on maxDiff condition
    adjList := make([][]int, n)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if abs(nums[i] - nums[j]) <= maxDiff {
                adjList[i] = append(adjList[i], j)
                adjList[j] = append(adjList[j], i)
            }
        }
    }
    
    // Function to perform BFS and find shortest path between two nodes
    bfs := func(start, end int) int {
        if start == end { return 0 }
        visited := make([]bool, n)
        queue := []int{start}
        dist := 0
        
        for len(queue) > 0 {
            dist++ // Increment distance at each level of BFS tree traversal
            nextQueue := []int{} // Hold next level nodes to visit in BFS tree traversal. 
            for _, node := range queue { // Process current level nodes in queue one by one. 
                for _, neighbor := range adjList[node] { // Traverse all neighbors of current node.  
                    if neighbor == end { return dist } // If neighbor is target node 'end', return distance as result. 
                    if !visited[neighbor] { // If neighbor node hasn't been visited yet, mark it visited and add it to nextQueue.  
                        visited[neighbor] = true // Mark neighbor as visited.
                        nextQueue = append(nextQueue, neighbor) // Add unvisited neighbors at current level into queue.
                    } 
                }
            }
            queue = nextQueue // Move queue pointer to next level nodes
        }
        return -1 // Return -1 if target is unreachable from start
    }

    // Process each query using BFS
    answer := make([]int, len(queries))
    for i, q := range queries {
        answer[i] = bfs(q[0], q[1])
    }
    return answer
}
# @lc code=end