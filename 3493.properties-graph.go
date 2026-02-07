# @lc code=start
func numberOfComponents(properties [][]int, k int) int {
    n := len(properties)
    adjList := make([][]int, n)

    // Define intersect function to calculate common distinct integers
    intersect := func(a, b []int) int {
        setA := make(map[int]struct{})
        for _, num := range a {
            setA[num] = struct{}{}
        }
        count := 0
        for _, num := range b {
            if _, exists := setA[num]; exists {
                count++
                delete(setA, num) // Ensure distinct counting
            }
        }
        return count
    }

    // Build adjacency list based on intersection condition
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if intersect(properties[i], properties[j]) >= k {
                adjList[i] = append(adjList[i], j)
                adjList[j] = append(adjList[j], i)
            }
        }
    }

    // Function for DFS traversal
    visited := make([]bool, n)
    var dfs func(int)
    dfs = func(node int) {
        visited[node] = true
        for _, neighbor := range adjList[node] {
            if !visited[neighbor] {
                dfs(neighbor)
            }
        }
    }

    // Count connected components using DFS
    components := 0
    for i := 0; i < n; i++ {
        if !visited[i] {
            dfs(i)
            components++
        }
    }

    return components
}
# @lc code=end