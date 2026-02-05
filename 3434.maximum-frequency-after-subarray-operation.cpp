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
        vector<int> diff(n);
        for (int i = 0; i < n; ++i) {
            diff[i] = k - nums[i];
        }
        int max_freq = 1, curr_freq = 1;
        for (int i = 1; i < n; ++i) {
            if (diff[i] == diff[i-1]) {
                curr_freq++;
                if (curr_freq > max_freq) max_freq = curr_freq;
            } else {
                curr_freq = 1;
            }
        }
        return max_freq;
    }
};
# @lc code=end