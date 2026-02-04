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
        stack<int> s;
        for (int i = n - 1; i >= 0; --i) {
            while (!s.empty() && nums[i] > nums[s.top()]) {
                steps[i] = max(steps[i] + 1, steps[s.top()]);
                s.pop();
            }
            s.push(i);
        }
        return *max_element(steps.begin(), steps.end());
    }
};
# @lc code=end