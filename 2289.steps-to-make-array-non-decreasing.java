#
# @lc app=leetcode id=2289 lang=java
#
# [2289] Steps to Make Array Non-decreasing
#
# @lc code=start
class Solution {
    public int totalSteps(int[] nums) {
        Stack<int[]> stack = new Stack<>(); // Stack to hold pairs of (number, steps)
        int maxSteps = 0;
        for (int i = nums.length - 1; i >= 0; i--) {
            int steps = 0;
            while (!stack.isEmpty() && stack.peek()[0] < nums[i]) {
                steps = Math.max(steps, stack.pop()[1]); // Remove smaller elements and calculate steps required for removal
            }
            if (!stack.isEmpty()) { // If a larger number exists ahead, increment step count
                steps++; 
            } 
            maxSteps = Math.max(maxSteps, steps); // Track max steps needed for any element
            stack.push(new int[]{nums[i], steps}); // Push current element with its step count onto stack
        } 
        return maxSteps; 
    } 
}
# @lc code=end