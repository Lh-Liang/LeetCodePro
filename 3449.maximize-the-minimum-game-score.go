//
// @lc app=leetcode id=3449 lang=golang
//
// [3449] Maximize the Minimum Game Score
//
// @lc code=start
func maxScore(points []int, m int) int64 {
    n := len(points)
    
    // Helper function to check feasibility of achieving a certain minimum value.
    isFeasible := func(target int) bool {
        totalMoves := 0
        currentScore := make([]int, n)
        for i := 0; i < n; i++ {
            if currentScore[i] < target {
                needed := target - currentScore[i]
                totalMoves += (needed + points[i] - 1) / points[i] // Ceiling division
            }
            if totalMoves > m {
                return false
            }
        }
        return true
    }
    
    left, right := 0, 1000000000 // Start with reasonable bounds for binary search based on constraints.
    var result int64 = 0
    
    for left <= right {
        mid := (left + right) / 2
        if isFeasible(mid) { // Check if mid can be achieved as minimum value.
            result = int64(mid) // If yes, update result.
            left = mid + 1 // Try for a better (higher) result.
        } else {
            right = mid - 1 // Otherwise, decrease the potential result range.
        } 
    } 
    return result 
a}
a // @lc code=end