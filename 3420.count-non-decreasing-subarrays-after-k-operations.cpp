#
# @lc app=leetcode id=3420 lang=cpp
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#
# @lc code=start
class Solution {
public:
    long long countNonDecreasingSubarrays(vector<int>& nums, int k) {
        int n = nums.size();
        long long count = 0;
        
        for (int i = 0; i < n; i++) {
            long long cost = 0;
            int max_val = nums[i];
            
            for (int j = i; j < n; j++) {
                if (nums[j] < max_val) {
                    cost += max_val - nums[j];
                } else {
                    max_val = nums[j];
                }
                
                if (cost <= k) {
                    count++;
                } else {
                    break;
                }
            }
        }
        
        return count;
    }
};
# @lc code=end