#
# @lc app=leetcode id=2289 lang=java
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution {
    public int totalSteps(int[] nums) {
        Stack<int[]> stack = new Stack<>(); // Element and its steps count
        int maxSteps = 0;
        for (int num : nums) {
            int currentSteps = 0;
            // Check if current number causes previous numbers in stack to be removed
            while (!stack.isEmpty() && stack.peek()[0] <= num) {
                currentSteps = Math.max(currentSteps, stack.pop()[1]);
            }
            // Calculate max steps needed to remove
            currentSteps = (stack.isEmpty()) ? 0 : currentSteps + 1;
            maxSteps = Math.max(maxSteps, currentSteps);
            // Push current number and its calculated steps onto the stack
            stack.push(new int[]{num, currentSteps});
        }
        return maxSteps;
    }
}
# @lc code=end