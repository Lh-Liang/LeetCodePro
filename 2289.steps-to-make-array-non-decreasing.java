#
# @lc app=leetcode id=2289 lang=java
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution {
    public int totalSteps(int[] nums) {
        int n = nums.length;
        int[] cnt = new int[n];
        java.util.Stack<Integer> stack = new java.util.Stack<>();
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int steps = 0;
            while (!stack.isEmpty() && nums[i] >= nums[stack.peek()]) {
                steps = Math.max(steps, cnt[stack.pop()]);
            }
            if (!stack.isEmpty()) {
                cnt[i] = steps + 1;
                ans = Math.max(ans, cnt[i]);
            }
            stack.push(i);
        }
        return ans;
    }
}
# @lc code=end