func totalSteps(nums []int) int {
    type pair struct {
        value int
        steps int
    }
    var stack []pair
    maxSteps := 0
    for i := len(nums) - 1; i >= 0; i-- {
        currentSteps := 0
        for len(stack) > 0 && nums[i] > stack[len(stack)-1].value {
            currentSteps = max(currentSteps+1, stack[len(stack)-1].steps)
            stack = stack[:len(stack)-1]
        }
        maxSteps = max(maxSteps, currentSteps)
        stack = append(stack, pair{nums[i], currentSteps})
    }
    return maxSteps
}

func max(a, b int) int { if a > b { return a } else { return b }}