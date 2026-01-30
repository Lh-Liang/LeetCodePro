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
        int total_k = 0;
        // current_gain[v] tracks the running Kadane sum for value v
        // max_gain[v] tracks the maximum subarray gain found for value v
        vector<int> current_gain(51, 0);
        vector<int> max_gain(51, 0);
        
        for (int x : nums) {
            if (x == k) {
                total_k++;
                // If we see k, it decreases the gain for all potential target values v
                for (int v = 1; v <= 50; ++v) {
                    if (v == k) continue;
                    current_gain[v]--;
                    // If current_gain falls below 0, reset (Standard Kadane's)
                    if (current_gain[v] < 0) current_gain[v] = 0;
                }
            } else if (x >= 1 && x <= 50) {
                // If we see x, it increases the gain for target value x
                current_gain[x]++;
                if (current_gain[x] > max_gain[x]) {
                    max_gain[x] = current_gain[x];
                }
            }
        }
        
        int best_overall_gain = 0;
        for (int v = 1; v <= 50; ++v) {
            if (v != k) {
                best_overall_gain = max(best_overall_gain, max_gain[v]);
            }
        }
        
        return total_k + best_overall_gain;
    }
};
# @lc code=end