#
# @lc app=leetcode id=3434 lang=cpp
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        long long totalOperations = 0;
        int left = 0;
        int maxFreq = 0;
        for (int right = 0; right < nums.size(); ++right) {
            totalOperations += nums[right];
            while ((right - left + 1) * nums[right] - totalOperations > k) {
                totalOperations -= nums[left];
                ++left;
            }
            maxFreq = max(maxFreq, right - left + 1);
        }
        return maxFreq;
    }
};
# @lc code=end