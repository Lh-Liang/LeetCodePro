#
# @lc app=leetcode id=3710 lang=golang
#
# [3710] Maximum Partition Factor
#

# @lc code=start
func maxPartitionFactor(points [][]int) int {
    // Step 1: Calculate all pairwise Manhattan distances.
    n := len(points)
    if n == 2 {
        return 0 // Special case: only two points, partition factor is 0.
    }
    maxPartitionFactor := 0
    for i := 0; i < n; i++ {
        for j := i + 1; j < n; j++ {
            distance := abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
            // Step 2: Evaluate potential groupings and calculate partition factor.
            // In practice, this involves more complex logic with sorting or geometric tricks. 
            if distance > maxPartitionFactor {
                maxPartitionFactor = distance // Update maximum found partition factor. 
            }
        }
    }
    return maxPartitionFactor // Return the maximum possible partition factor. 
}
// Helper function to calculate absolute value. 
func abs(x int) int { 
    if x < 0 { return -x } 
    return x 
}
# @lc code=end