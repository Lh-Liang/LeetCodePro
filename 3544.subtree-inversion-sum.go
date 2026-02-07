#
# @lc app=leetcode id=3544 lang=golang
#
# [3544] Subtree Inversion Sum
#

# @lc code=start
func subtreeInversionSum(edges [][]int, nums []int, k int) int64 {
    // Step 1: Convert edges into an adjacency list for easy tree traversal.
    adjList := make(map[int][]int)
    for _, edge := range edges {
        u, v := edge[0], edge[1]
        adjList[u] = append(adjList[u], v)
        adjList[v] = append(adjList[v], u)
    }

    // Step 2: Implement DFS with dynamic programming to calculate potential sums.
    var dfs func(node, parent int) (sumWithoutInversion, sumWithInversion int64)
    dfs = func(node, parent int) (sumWithoutInversion, sumWithInversion int64) {
        currentSum := int64(nums[node])
        invertedSum := -currentSum
        
        for _, neighbor := range adjList[node] {
            if neighbor == parent { continue }
            childWithoutInv, childWithInv := dfs(neighbor, node)
            currentSum += max(childWithoutInv, childWithInv)
            invertedSum += max(-childWithoutInv, -childWithInv) // Invert child sums as well.
        }
        return currentSum, invertedSum + 2*int64(nums[node]) // Inverting root node itself.
    }

    // Step 3: Start DFS from root node 0 considering all constraints.
    resultWithoutInversion, resultWithInversion := dfs(0, -1)
    return max(resultWithoutInversion, resultWithInversion) // Return the maximum possible sum.
}
# @lc code=end