#
# @lc app=leetcode id=3782 lang=golang
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#
# @lc code=start
func lastInteger(n int64) int64 {
    head := int64(1)
    step := int64(1)
    left := true
    remaining := n
    for remaining > 1 {
        if left || remaining%2 == 1 {
            head += step
        }
        remaining /= 2
        step *= 2
        left = !left
    }
    return head
}
# @lc code=end