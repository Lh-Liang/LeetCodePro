#
# @lc app=leetcode id=2289 lang=golang
#
# [2289] Steps to Make Array Non-decreasing
#
# @lc code=start
func totalSteps(nums []int) int {
    n := len(nums)
    stack := make([][2]int, 0) // Each entry: [value, steps]
    res := 0
    for i := n - 1; i >= 0; i-- {
        steps := 0
        for len(stack) > 0 && nums[i] > stack[len(stack)-1][0] {
            steps = max(steps+1, stack[len(stack)-1][1])
            stack = stack[:len(stack)-1]
        }
        res = max(res, steps)
        stack = append(stack, [2]int{nums[i], steps})
    }
    return res
}

func max(a, b int) int {
    if a > b {
        return a
    }
    return b
}
# @lc code=end