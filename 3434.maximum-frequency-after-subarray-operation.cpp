#
# @lc app=leetcode id=3434 lang=cpp
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int initial_k_count = 0;
        for (int x : nums) {
            if (x == k) initial_k_count++;
        }
        
        int max_gain = 0;
        // Iterate through all possible values v (1-50) that could be transformed into k.
        for (int v = 1; v <= 50; ++v) {
            if (v == k) continue;
            
            int current_running_gain = 0;
            int local_max_gain = 0;
            
            // Kadane's algorithm to find the subarray maximizing (count(v) - count(k))
            for (int x : nums) {
                if (x == v) {
                    current_running_gain++;
                } else if (x == k) {
                    current_running_gain--;
                }
                
                if (current_running_gain < 0) {
                    current_running_gain = 0;
                }
                if (current_running_gain > local_max_gain) {
                    local_max_gain = current_running_gain;
                }
            }
            max_gain = max(max_gain, local_max_gain);
        }
        
        return initial_k_count + max_gain;
    }
};
# @lc code=end