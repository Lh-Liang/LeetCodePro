#
# @lc app=leetcode id=3449 lang=golang
#
# [3449] Maximize the Minimum Game Score
#
# @lc code=start
func maxScore(points []int, m int) int64 {
    n := len(points)
    left, right := 0, int(1e18) // Setting high right bound due to constraints
    
    check := func(minVal int64) bool {
        moves := int64(0)
        for _, point := range points {
            if point < minVal {
                moves += minVal - int64(point)
            }
        }
        return moves <= int64(m)
    }
    
    for left < right { // Binary search for maximum possible minimum score
        mid := (left + right + 1) / 2
        if check(mid) {
            left = mid // Try for a higher minimum score if possible
        } else {
            right = mid - 1 // Reduce the maximum possible score when condition fails
        }
    }
    return int64(left) // This will be our answer since it maximizes our minimum game score.
}
# @lc code=end