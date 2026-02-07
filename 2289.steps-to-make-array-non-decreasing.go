#
# @lc app=leetcode id=2289 lang=golang
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
func totalSteps(nums []int) int {
    stack := [][]int{} // Stack stores pairs: value and step count
    maxSteps := 0 // Track maximum steps required overall
    for _, num := range nums {
        count := 0 // Steps for current number
        // Compare with elements in stack and pop those less or equal to current
        while len(stack) > 0 && stack[len(stack)-1][0] <= num {
            count = max(count, stack[len(stack)-1][1]) // Get max step count from popped elements
            stack = stack[:len(stack)-1] // Remove top element as it's not blocking anymore
        }
        if len(stack) > 0 {
            count++ // Increment step as there are larger numbers before it that will cause removal in future steps
        }
        // Push current number with calculated step count onto stack
        stack = append(stack, []int{num, count})
        maxSteps = max(maxSteps, count) // Update overall max steps if needed
    }
    return maxSteps 
}
// Helper function to get maximum value between two integers 
func max(a, b int) int { 
    if a > b { 
        return a 
    } 
    return b 
}
# @lc code=end