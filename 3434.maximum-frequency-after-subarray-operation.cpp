#include <vector>
#include <algorithm>

using namespace std;

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
        // Iterate through all possible values v that could be converted to k
        for (int v = 1; v <= 50; ++v) {
            if (v == k) continue;
            
            int current_gain = 0;
            int local_max_gain = 0;
            for (int x : nums) {
                if (x == v) {
                    current_gain++;
                } else if (x == k) {
                    current_gain--;
                }
                
                // Kadane's algorithm logic
                if (current_gain < 0) {
                    current_gain = 0;
                }
                if (current_gain > local_max_gain) {
                    local_max_gain = current_gain;
                }
            }
            max_gain = max(max_gain, local_max_gain);
        }
        
        return initial_k_count + max_gain;
    }
};
# @lc code=end