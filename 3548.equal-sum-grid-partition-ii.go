#
# @lc app=leetcode id=3548 lang=golang
#
# [3548] Equal Sum Grid Partition II
#

# @lc code=start
func canPartitionGrid(grid [][]int) bool {
    m, n := len(grid), len(grid[0])
    totalSum := 0
    rowSums := make([]int, m)
    colSums := make([]int, n)
    
    // Calculate total sum and row/column prefix sums
    for i := 0; i < m; i++ {
        for j := 0; j < n; j++ {
            totalSum += grid[i][j]
            rowSums[i] += grid[i][j]
            colSums[j] += grid[i][j]
        }
    }
    
    // If total sum is odd, it's impossible to partition equally
    if totalSum % 2 != 0 {
        return false
    }
    equalSum := totalSum / 2
    
    // Check horizontal cuts with prefix sums
    currentTopSum := 0
    for i := 0; i < m-1; i++ {
        currentTopSum += rowSums[i]
        if checkEqualWithDiscount(currentTopSum, equalSum, grid) {
            return true
        }
    }
    
    // Check vertical cuts with prefix sums
    currentLeftSum := 0
    for j := 0; j < n-1; j++ {
        currentLeftSum += colSums[j]
        if checkEqualWithDiscount(currentLeftSum, equalSum, grid) {
            return true
        }
    }
    
    return false
}

func checkEqualWithDiscount(sectionSum int, target int, grid [][]int) bool {	   difference := abs(sectionSum - target)	   	   // Iterate over all cells to find a suitable discount	   for i := range grid {	       for j := range grid[i] {	           if difference == 0 || difference == grid[i][j] {	               if ensureConnectednessAfterDiscount(grid, i, j) {	                   return true	               }	           }	       }	   }	   return false	}
bool ensureConnectednessAfterDiscount(grid [][]int, x int, y int) bool {   // Implement flood-fill or BFS/DFS from any non-discounted cell   // Check connectivity of both partitioned sections   return true}
bool abs(x int) int { if x < 0 { return -x } else { return x } }