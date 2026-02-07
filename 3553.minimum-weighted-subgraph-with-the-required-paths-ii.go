#
# @lc app=leetcode id=3553 lang=golang
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
func minimumWeight(edges [][]int, queries [][]int) []int {
    // Convert edge list to adjacency list
    adjList := make(map[int][][2]int)
    for _, edge := range edges {
        u, v, w := edge[0], edge[1], edge[2]
        adjList[u] = append(adjList[u], [2]int{v, w})
        adjList[v] = append(adjList[v], [2]int{u, w})
    }
    
    // Function to perform BFS and return distances from a source node
    bfs := func(source int) map[int]int {
        dist := make(map[int]int)
        for node := range adjList { dist[node] = int(1e9) } // Use a large number as infinity
        queue := []int{source}
        dist[source] = 0
        
        for len(queue) > 0 {
            node := queue[0]
            queue = queue[1:]
            for _, neighbor := range adjList[node] {
                nextNode, weight := neighbor[0], neighbor[1]
                if dist[node] + weight < dist[nextNode] {
                    dist[nextNode] = dist[node] + weight
                    queue = append(queue, nextNode)
                }
            }
        }
        return dist
    }
    
    // Answer queries by finding minimum subtrees connecting sources to destination
    results := make([]int, len(queries))
    for i, q := range queries {
        src1, src2, dest := q[0], q[1], q[2]
        distFromSrc1 := bfs(src1) "// Get distances from src1 node