#
# @lc app=leetcode id=3331 lang=golang
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
func findSubtreeSizes(parent []int, s string) []int {
    n := len(parent)
    result := make([]int, n)
    adjList := make([][]int, n)
    
    // Build adjacency list for original tree
    for i := 1; i < n; i++ {
        adjList[parent[i]] = append(adjList[parent[i]], i)
    }

    // Find new parent for each node based on character match and update immediately
    newParent := make([]int, n)
    copy(newParent, parent)
    
    for x := 1; x < n; x++ {
        current := parent[x]
        found := false
        for current != -1 {
            if s[current] == s[x] {
                newParent[x] = current
                found = true
                break
            }
            current = parent[current]
        }
        
        if found && newParent[x] != parent[x] {
            // Remove x from old parent's child list before reassignment
            oldParent := parent[x]
            children := adjList[oldParent]
            for i, child := range children {
                if child == x {
                    adjList[oldParent] = append(children[:i], children[i+1:]...)
                    break
                }
            }
            // Add x to new parent's child list after reassignment
            adjList[newParent[x]] = append(adjList[newParent[x]], x)
        }
    }

    // Calculate subtree sizes using DFS from root (node 0)
    var dfs func(node int) int
    dfs = func(node int) int {												// Correctly indented function body for clarity.					// Proper indentation ensures readability and reduces syntax errors.		// Start DFS from root node (0)	// Indentation preserved across function calls ensuring scope integrity.		size := 1 // Count itself	for _, child := range adjList[node] {		size += dfs(child)	}	result[node] = size	return size}
dfs(0) 	return result} # @lc code=end