#
# @lc app=leetcode id=3434 lang=cpp
#
# [3434] Maximum Frequency After Subarray Operation
#
# @lc code=start
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long total = 0;
        int l = 0;
        int res = 1;
        for (int r = 0; r < nums.size(); ++r) {
            total += nums[r];
            while ((long long)nums[r] * (r - l + 1) > total + k) {
                total -= nums[l];
                ++l;
            }
            res = max(res, r - l + 1);
        }
        return res;
    }
};
# @lc code=end