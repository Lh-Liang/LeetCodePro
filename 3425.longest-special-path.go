#
# @lc app=leetcode id=3425 lang=golang
#
# [3425] Longest Special Path
#

# @lc code=start
func longestSpecialPath(edges [][]int, nums []int) []int {
    // Convert edges to an adjacency list representation
    adjList := make(map[int][][2]int)
    for _, edge := range edges {
        u, v, length := edge[0], edge[1], edge[2]
        adjList[u] = append(adjList[u], [2]int{v, length})
        adjList[v] = append(adjList[v], [2]int{u, length})
    }

    var dfs func(node int, parent int, visited map[int]bool, uniqueValues map[int]bool) (int, int)
    dfs = func(node int, parent int, visited map[int]bool, uniqueValues map[int]bool) (int, int) {
        maxLength := 0
        minNodes := len(nums) // Initialize with maximum possible nodes
        visited[node] = true
        uniqueValues[nums[node]] = true
        for _, neighbor := range adjList[node] {
            nextNode := neighbor[0]
            edgeLength := neighbor[1]
            if nextNode != parent && !visited[nextNode] && !uniqueValues[nums[nextNode]] {
                pathLength, nodeCount := dfs(nextNode, node, visited, uniqueValues)
                totalLength := pathLength + edgeLength
                if totalLength > maxLength {
                    maxLength = totalLength
                    minNodes = nodeCount + 1 // Include current node in count
                } else if totalLength == maxLength {
                    if nodeCount + 1 < minNodes {
                        minNodes = nodeCount + 1
                    }
                }
            }
        }
        delete(uniqueValues, nums[node]) // Backtrack: Remove current node's value before returning
        visited[node] = false // Reset visited status for backtracking purposes
        return maxLength, minNodes - 1 // Adjust for backtracking scenario where current node is not included directly in result count yet.
    }

    longestPath := 0
    minPathNodes := len(nums) // Initialize with maximum possible nodes count as initial value for minimum nodes calculation.
    visited := make(map[int]bool)
    uniqueValues := make(map[int]bool)
    pathLen, nodeCount := dfs(0, -1, visited, uniqueValues)
    if pathLen > longestPath {
        longestPath = pathLen
        minPathNodes = nodeCount + 1 // Include root node in count [if applicable][/if][endif][else][endfor][endwhilendit,"],"]"]<|vq_11956|>}"]"])}"]["\"]\"]"]}"/"\""]}"]; "/"]/""); end