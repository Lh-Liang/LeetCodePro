#
# @lc app=leetcode id=3704 lang=golang
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
func countNoZeroPairs(n int64) int64 {
    var isNoZero func(int64) bool = func(x int64) bool {
        for x > 0 {
            if x%10 == 0 {
                return false
            }
            x /= 10
        }
        return true
    }
    count := int64(0)
    for a := int64(1); a < n; a++ {
        b := n - a
        if isNoZero(a) && isNoZero(b) {
            count++
        }
    }
    return count
}
# @lc code=end