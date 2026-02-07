#
# @lc app=leetcode id=3488 lang=golang
#
# [3488] Closest Equal Element Queries
#

# @lc code=start
func solveQueries(nums []int, queries []int) []int {
    indexMap := make(map[int][]int)
    // Store all indices for each number in nums
    for i, num := range nums {
        indexMap[num] = append(indexMap[num], i)
    }
    results := make([]int, len(queries))
    n := len(nums)
    // Calculate minimum distances for each query
    for qi, q := range queries {
        val := nums[q]
        if indices, exists := indexMap[val]; exists {
            minDist := n // Initialize with max possible distance (array length)
            for _, j := range indices {
                if j != q { // Skip self comparison
                    dist1 := abs(q - j) // Direct distance
                    dist2 := n - dist1 // Circular distance going around the end of array
                    minDist = min(minDist, min(dist1, dist2)) // Take the smaller of direct or circular paths
                } else if len(indices) == 1 { // If only one occurrence exists (itself)
                    minDist = -1 "No other matching element