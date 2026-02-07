#
# @lc app=leetcode id=3449 lang=golang
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
func maxScore(points []int, m int) int64 {
    // Step 1: Define the binary search boundaries
    left, right := int64(0), int64(0)
    for _, v := range points {
        right += int64(v)
    }
    n := len(points)
    // Step 2: Implement a helper to check if each gameScore can reach at least 'minScore' in at most m moves
    var canAchieve = func(minScore int64) bool {
        // For each position, we want at least minScore
        // To minimize moves, always give minScore//points[i] (rounded up) visits to i
        totalMoves := int64(0)
        for _, p := range points {
            need := (minScore + int64(p) - 1) / int64(p)
            totalMoves += need
        }
        // The minimal totalMoves required is the sum above
        // But since we start at -1 and can move left/right, minimal path covers n-1 (to reach the end), so m >= totalMoves + (n-1) - n
        // But since each move can be used flexibly, just check totalMoves <= int64(m)
        return totalMoves <= int64(m)
    }
    // Step 3: Use binary search to maximize minScore
    ans := int64(0)
    for left <= right {
        mid := left + (right-left)/2
        if canAchieve(mid) {
            ans = mid
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    // Step 4: Ensure all reasoning steps are reflected in the code
    return ans
}
# @lc code=end