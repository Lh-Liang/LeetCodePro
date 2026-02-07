// @lc app=leetcode id=2289 lang=cpp
//
// [2289] Steps to Make Array Non-decreasing
//
// @lc code=start
class Solution {
public:
    int totalSteps(vector<int>& nums) {
        vector<int> dp(nums.size(), 0);
        stack<int> st;
        int max_steps = 0;
        for (int i = 0; i < nums.size(); ++i) {
            while (!st.empty() && nums[st.top()] <= nums[i]) {
                dp[i] = max(dp[i], dp[st.top()] + 1);
                st.pop();
            }
            max_steps = max(max_steps, dp[i]);
            st.push(i);
        }
        return max_steps;
    }
};
// @lc code=end