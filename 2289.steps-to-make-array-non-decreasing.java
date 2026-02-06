#
# @lc app=leetcode id=2289 lang=java
#
# [2289] Steps to Make Array Non-decreasing
#
# @lc code=start
class Solution {
    public int totalSteps(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];
        int res = 0;
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        for (int i = 0; i < n; ++i) {
            int maxSteps = 0;
            while (!stack.isEmpty() && nums[i] >= nums[stack.peek()]) {
                maxSteps = Math.max(maxSteps, dp[stack.pop()]);
            }
            if (!stack.isEmpty()) {
                dp[i] = maxSteps + 1;
                res = Math.max(res, dp[i]);
            }
            stack.push(i);
        }
        return res;
    }
}
# @lc code=end