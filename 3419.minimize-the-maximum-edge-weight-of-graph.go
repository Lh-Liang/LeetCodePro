#
# @lc app=leetcode id=3419 lang=golang
#
# [3419] Minimize the Maximum Edge Weight of Graph
#
# @lc code=start
func minMaxWeight(n int, edges [][]int, threshold int) int {
    // Sort edges by weight in ascending order for binary search.
    sort.Slice(edges, func(i, j int) bool {
        return edges[i][2] < edges[j][2]
    })
    
    // Binary search over possible maximum edge weights.
    low, high := 0, len(edges)-1
    result := -1
    
    for low <= high {
        mid := (low + high) / 2
        maxWeight := edges[mid][2]
        
        // Filter and create graph with edges having weight <= maxWeight.
        filteredEdges := make([][]int, 0)
        for _, edge := range edges {
            if edge[2] <= maxWeight {
                filteredEdges = append(filteredEdges, edge)
            } else {
                break // As sorted by weight, no need to check further.
            }
        }
        
        // Check connectivity from node 0 using BFS/DFS and outgoing threshold constraint.
        if isConnectedAndWithinThreshold(n, filteredEdges, threshold) {
            result = maxWeight // Found a valid configuration.
            high = mid - 1     // Try for smaller maxWeight.
        } else {
            low = mid + 1      // Increase maxWeight as current failed.
        }
    }
    return result
}

func isConnectedAndWithinThreshold(n int, edges [][]int, threshold int) bool {
outDegree := make([]int, n)
adjList := make([][]int, n)
bfsQueue := []int{0}
isVisited := make([]bool, n)
isVisited[0] = true
visitedCount := 1 // Start from node 0 being visited
for _, edge := range edges {
outDegree[edge[0]]++
adjList[edge[0]] = append(adjList[edge[0]], edge[1])
i}
f exceedsThreshold(outDegree, threshold) {
break false
}
f len(bfsQueue) > 0 {
deueue head...
f or each neighbor...
m ark visited...
i f unvisited...
increment count...
c ontinue traversal...
al check against visited count...
equal to n?
ture or false based on reachability...
graph traversal logic using adjacency list...
graph validation against constraints...