#
# @lc app=leetcode id=3605 lang=golang
#
# [3605] Minimum Stability Factor of Array
#

# @lc code=start
import (
    "math"
)

func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a % b
    }
    return a
}

// (Implementation outline, not full code)
func minStable(nums []int, maxC int) int {
    n := len(nums)
    left, right := 1, n
    answer := n
    
    // Precompute sparse table or segment tree for GCD queries
    // ...

    // Helper: Checks if we can eliminate all stable subarrays of length >= k with <= maxC modifications
    isPossible := func(k int) bool {
        // 1. For all windows of length k, get GCD efficiently
        // 2. For those with GCD >= 2, treat as intervals [i, i+k-1]
        // 3. Use greedy interval covering: sort intervals by end, greedily select covering points
        // 4. Count minimal number of points required, compare to maxC
        // Return true if feasible, false otherwise
        return true // placeholder
    }
    
    for left <= right {
        mid := (left + right) / 2
        if isPossible(mid) {
            answer = mid
            right = mid - 1
        } else {
            left = mid + 1
        }
    }
    return answer
}
# @lc code=end