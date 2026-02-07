#
# @lc app=leetcode id=2289 lang=golang
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
func totalSteps(nums []int) int {
    n := len(nums)
    steps := make([]int, n)
    stack := []int{}
    maxSteps := 0
    for i := n - 1; i >= 0; i-- {
        for len(stack) > 0 && nums[i] > nums[stack[len(stack)-1]] {
            steps[i] = max(steps[i]+1, steps[stack[len(stack)-1]])
            stack = stack[:len(stack)-1]
        }
        maxSteps = max(maxSteps, steps[i])
        stack = append(stack, i)
    }
    return maxSteps
}
func max(a, b int) int { if a > b { return a } else { return b } }