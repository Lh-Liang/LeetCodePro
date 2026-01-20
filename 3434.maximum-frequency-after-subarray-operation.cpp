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
    /**
     * The problem asks to maximize the frequency of k after applying one subarray operation.
     * By adding x to nums[i..j], we can transform some value v into k.
     * The total count of k becomes: (Total k's in nums) - (k's in subarray) + (v's in subarray).
     * We want to find a subarray [i, j] and a value v that maximizes (v's in subarray - k's in subarray).
     * This is the Maximum Subarray Sum problem where v contributes +1 and k contributes -1.
     */
    int maxFrequency(vector<int>& nums, int k) {
        int total_k = 0;
        int max_gain = 0;
        // current_gain[v] stores the Kadane's algorithm state for each possible value v in [1, 50].
        vector<int> current_gain(51, 0);

        for (int x : nums) {
            if (x == k) {
                total_k++;
                // If the current element is k, it decreases the gain for all potential target values v.
                for (int v = 1; v <= 50; ++v) {
                    if (current_gain[v] > 0) {
                        current_gain[v]--;
                    }
                }
            } else {
                // If the current element is x, it increases the potential gain for value v = x.
                current_gain[x]++;
                if (current_gain[x] > max_gain) {
                    max_gain = current_gain[x];
                }
            }
        }

        return total_k + max_gain;
    }
};
# @lc code=end