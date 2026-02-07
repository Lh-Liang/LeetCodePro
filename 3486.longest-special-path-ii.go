#
# @lc app=leetcode id=3486 lang=golang
#
# [3486] Longest Special Path II
#

# @lc code=start
func longestSpecialPath(edges [][]int, nums []int) []int {
    type Node struct {
        id int
        length int
    }
    n := len(nums)
    graph := make([][]Node, n)
    for _, edge := range edges {
        u, v, length := edge[0], edge[1], edge[2]
        graph[u] = append(graph[u], Node{id: v, length: length})
        graph[v] = append(graph[v], Node{id: u, length: length})
    }
    
    var dfs func(node int, parent int, path map[int]int) (int, int)
    dfs = func(node int, parent int, path map[int]int) (int, int) {
        maxPathLength := 0
        minNodes := n // Start with max nodes possible for comparison
        
        newPath := make(map[int]int)
        for k, v := range path {
            newPath[k] = v
        }
        newPath[nums[node]]++
      
        distinctCount := len(newPath)
        duplicates := 0 // Track duplicates separately with a counter
        for _, count := range newPath {
            if count > 1 {
                duplicates++
            }
        }
      
        if duplicates > 1 { // More than one duplicate invalidates this path branch
            return 0, n // Invalid path returns zero length and max nodes (to be ignored)
        }
      
        for _, neighbor := range graph[node] {
            if neighbor.id == parent {
                continue // Avoid revisiting parent node in DFS
            }
            
            length, nodes := dfs(neighbor.id, node, newPath)
          totalLength := length + neighbor.length // Accumulate edge lengths in path computation
          if totalLength > maxPathLength || (totalLength == maxPathLength && nodes < minNodes) {
              maxPathLength = totalLength
              minNodes = nodes + 1 // Include current node in count
          }
      }
      return maxPathLength, minNodes
   }
   
   resultLength := 0
   resultNodes := n // Start with max nodes possible for initialization comparison purposes
   
   length, nodes := dfs(0, -1, map[int]int{}) // Start DFS from root node (node 0)
   if length > resultLength || (length == resultLength && nodes < resultNodes) {
       resultLength = length
       resultNodes = nodes
   }
   return []int{resultLength, resultNodes}
in}
in# @lc code=end