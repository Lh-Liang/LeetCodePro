#
# @lc app=leetcode id=2289 lang=cpp
#
# [2289] Steps to Make Array Non-decreasing
#
# @lc code=start
class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size();
        vector<int> dp(n, 0);
        stack<int> stk;
        int result = 0;
        
        for (int i = 0; i < n; i++) {
            int maxSteps = 0;
            while (!stk.empty() && nums[stk.top()] <= nums[i]) {
                maxSteps = max(maxSteps, dp[stk.top()]);
                stk.pop();
            }
            
            if (!stk.empty()) {
                dp[i] = maxSteps + 1;
                result = max(result, dp[i]);
            }
            
            stk.push(i);
        }
        
        return result;
    }
};
# @lc code=end