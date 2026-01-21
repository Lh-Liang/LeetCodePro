#
# @lc app=leetcode id=3434 lang=cpp
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int n = nums.size();
        int total_k = 0;
        for (int num : nums) {
            if (num == k) ++total_k;
        }
        int max_gain = 0;
        for (int v = 1; v <= 50; ++v) {
            if (n == 0) continue;
            int delta = (nums[0] == v ? 1 : 0) - (nums[0] == k ? 1 : 0);
            int max_ending = delta;
            int max_s = delta;
            for (int i = 1; i < n; ++i) {
                delta = (nums[i] == v ? 1 : 0) - (nums[i] == k ? 1 : 0);
                max_ending = max(delta, max_ending + delta);
                max_s = max(max_s, max_ending);
            }
            if (max_s > max_gain) max_gain = max_s;
        }
        return total_k + max_gain;
    }
};
# @lc code=end