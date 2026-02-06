#
# @lc app=leetcode id=2289 lang=java
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution {
    public int totalSteps(int[] nums) {
        int n = nums.length;
        // Stack for holding indices of elements in nums
        Stack<Integer> stack = new Stack<>();
        // Array for tracking steps required for each element
        int[] steps = new int[n];
        // Iterate through each element in nums
        for (int i = 0; i < n; i++) {
            // While stack is not empty and current num is less than num at top index of stack
            while (!stack.isEmpty() && nums[stack.peek()] <= nums[i]) {
                steps[i] = Math.max(steps[i], steps[stack.pop()] + 1);
            }
            // Push current index onto stack for future comparisons
            stack.push(i);
        }
        // Max value in steps array is our result, representing maximum deletions required for any element. 
        return Arrays.stream(steps).max().orElse(0); 
    } 
}
# @lc code=end