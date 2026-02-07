#
# @lc app=leetcode id=3464 lang=golang
#
# [3464] Maximize the Distance Between Points on a Square
#

# @lc code=start
func maxDistance(side int, points [][]int, k int) int {
    // Binary search on possible distances
    var low, high = 0, side * 2
    var result = 0
    
    // Helper function to check if we can select k points with at least 'dist' apart
    feasible := func(dist int) bool {
        // Implement BFS or greedy method here
        return true // placeholder
    }
    
    for low <= high {
        mid := (low + high) / 2
        if feasible(mid) {
            result = mid // store mid as valid result because we are maximizing
            low = mid + 1 // try for larger minimum distance
        } else {
            high = mid - 1 // reduce the searched space if not feasible
        }
    }
    return result
}
// @lc code=end