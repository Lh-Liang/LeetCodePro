#
# @lc app=leetcode id=3434 lang=cpp
#
# [3434] Maximum Frequency After Subarray Operation
#
# @lc code=start
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        // Count initial frequency of k
        int base_count = 0;
        for (int num : nums) {
            if (num == k) base_count++;
        }
        
        int max_freq = base_count;
        
        // Try converting each unique value to k
        set<int> unique_values(nums.begin(), nums.end());
        for (int target_value : unique_values) {
            if (target_value == k) continue;
            
            // Use Kadane's algorithm to find the best subarray
            // contribution = +1 if we convert target_value to k
            // contribution = -1 if we lose an existing k
            int max_gain = 0;
            int current_sum = 0;
            for (int num : nums) {
                int contribution = 0;
                if (num == target_value) contribution = 1;
                else if (num == k) contribution = -1;
                
                current_sum = max(0, current_sum + contribution);
                max_gain = max(max_gain, current_sum);
            }
            
            max_freq = max(max_freq, base_count + max_gain);
        }
        
        return max_freq;
    }
};
# @lc code=end