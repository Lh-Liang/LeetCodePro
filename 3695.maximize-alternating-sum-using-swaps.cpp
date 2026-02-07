#
# @lc app=leetcode id=3695 lang=cpp
#
# [3695] Maximize Alternating Sum Using Swaps
#
# @lc code=start
class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums, vector<vector<int>>& swaps) {
        // Sort nums in descending order
        sort(nums.begin(), nums.end(), greater<int>());
        // Rearrange into alternating pattern starting from largest at even indices
        long long maxSum = 0;
        for (int i = 0; i < nums.size(); ++i) {
            if (i % 2 == 0) {
                maxSum += nums[i]; // Add for even indices
            } else {
                maxSum -= nums[i]; // Subtract for odd indices
            }
        }
        return maxSum;
    }
};
# @lc code=end