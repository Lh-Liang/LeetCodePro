#
# @lc app=leetcode id=2289 lang=cpp
#
# [2289] Steps to Make Array Non-decreasing
#

# @lc code=start
class Solution {
public:
    int totalSteps(vector<int>& nums) {
        int n = nums.size(), ans = 0;
        stack<pair<int, int>> st; // pair: value, steps needed
        for (int i = 0; i < n; ++i) {
            int maxT = 0;
            while (!st.empty() && nums[i] >= st.top().first) {
                maxT = max(maxT, st.top().second);
                st.pop();
            }
            int step = st.empty() ? 0 : maxT + 1;
            ans = max(ans, step);
            st.push({nums[i], step});
        }
        return ans;
    }
};
# @lc code=end