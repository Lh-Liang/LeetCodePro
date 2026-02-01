#
# @lc app=leetcode id=3434 lang=cpp
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int k_count = 0;
        for (int x : nums) {
            if (x == k) k_count++;
        }
        
        int max_gain = 0;
        // The values of nums[i] and k are between 1 and 50.
        // Iterate over all possible values v that could be transformed into k.
        for (int v = 1; v <= 50; ++v) {
            if (v == k) continue;
            
            int current_gain = 0;
            int best_gain_for_v = 0;
            for (int x : nums) {
                if (x == v) {
                    current_gain++;
                } else if (x == k) {
                    current_gain--;
                }
                
                if (current_gain < 0) {
                    current_gain = 0;
                }
                if (current_gain > best_gain_for_v) {
                    best_gain_for_v = current_gain;
                }
            }
            if (best_gain_for_v > max_gain) {
                max_gain = best_gain_for_v;
            }
        }
        
        return k_count + max_gain;
    }
};
# @lc code=end