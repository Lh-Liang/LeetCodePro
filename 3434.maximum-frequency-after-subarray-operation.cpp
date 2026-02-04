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
        int left = 0, right = 0;
        long long total = 0;
        int maxFreq = 0;
        while (right < nums.size()) {
            total += nums[right];
            while ((right - left + 1) * nums[right] - total > k) {
                total -= nums[left];
                left++;
            }
            maxFreq = max(maxFreq, right - left + 1);
            right++;
        }
        return maxFreq;
    }
};
# @lc code=end