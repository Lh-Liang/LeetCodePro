#
# @lc app=leetcode id=3434 lang=cpp
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int total_k = 0;
        bool present[52] = {false};
        for (int x : nums) {
            if (x == k) total_k++;
            present[x] = true;
        }

        int max_freq = total_k;

        // Try to convert each possible value v into k
        for (int v = 1; v <= 50; ++v) {
            if (v == k || !present[v]) continue;

            // Kadane's algorithm to find max subarray sum
            // where value v contributes +1 and value k contributes -1
            int current_sum = 0;
            int max_diff = 0;

            for (int x : nums) {
                if (x == v) {
                    current_sum += 1;
                } else if (x == k) {
                    current_sum -= 1;
                }
                
                if (current_sum < 0) {
                    current_sum = 0;
                }
                
                if (current_sum > max_diff) {
                    max_diff = current_sum;
                }
            }
            
            if (total_k + max_diff > max_freq) {
                max_freq = total_k + max_diff;
            }
        }

        return max_freq;
    }
};
# @lc code=end