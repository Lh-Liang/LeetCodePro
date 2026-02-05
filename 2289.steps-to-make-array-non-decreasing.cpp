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
        vector<int> steps(n, 0);
        stack<int> st;
        int res = 0;
        for (int i = 0; i < n; ++i) {
            int curr_steps = 0;
            while (!st.empty() && nums[i] > nums[st.top()]) {
                curr_steps = max(curr_steps + 1, steps[st.top()]);
                st.pop();
            }
            if (!st.empty()) {
                steps[i] = curr_steps;
                res = max(res, steps[i]);
            }
            st.push(i);
        }
        return res;
    }
};
# @lc code=end