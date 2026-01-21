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
        vector<int> steps(n);
        stack<int> st;
        const int INF = 2000000000;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            int cur_max = 0;
            while (!st.empty() && nums[st.top()] <= nums[i]) {
                int k = st.top(); st.pop();
                cur_max = max(cur_max, steps[k]);
            }
            if (!st.empty()) {
                steps[i] = 1 + cur_max;
                ans = max(ans, steps[i]);
            } else {
                steps[i] = INF;
            }
            st.push(i);
        }
        return ans;
    }
};
# @lc code=end