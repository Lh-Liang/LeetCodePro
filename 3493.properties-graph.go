#
# @lc app=leetcode id=3493 lang=golang
#
# [3493] Properties Graph
#
# @lc code=start
func numberOfComponents(properties [][]int, k int) int {
    n := len(properties)
    // Step 1: Define intersect function
    intersect := func(a, b []int) int {
        setA := make(map[int]struct{})
        for _, val := range a {
            setA[val] = struct{}{}
        }
        count := 0
        for _, val := range b {
            if _, found := setA[val]; found {
                count++
            }
        }
        return count
    }
    // Step 2: Build adjacency list based on intersect criteria (>= k)
    adjList := make([][]int, n)
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            if intersect(properties[i], properties[j]) >= k {
                adjList[i] = append(adjList[i], j)
                adjList[j] = append(adjList[j], i) // undirected graph 
            } 
        } 
    } 
    // Step 3: Use DFS/BFS to find connected components & count them & return result & boolean array visited initialized as false & componentCount initialized as zero & inside dfs function in all adjacent nodes if not visited then call dfs function again with that node as argument & increment componentCount by one for each node that is not visited at first and return componentCount