#
# @lc app=leetcode id=3779 lang=cpp
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#

# @lc code=start
#include <vector>

class Solution {
public:
    int minOperations(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;

        // Use a boolean array to track seen elements (values are up to 10^5)
        std::vector<bool> seen(100001, false);
        int last_dup_idx = -1;

        // Iterate from right to left to find the rightmost index 'i' 
        // that is part of a duplicate pair (i.e., nums[i] appears later).
        for (int i = n - 1; i >= 0; --i) {
            if (seen[nums[i]]) {
                last_dup_idx = i;
                break;
            }
            seen[nums[i]] = true;
        }

        // If no duplicates were found, 0 operations are needed.
        if (last_dup_idx == -1) {
            return 0;
        }

        // To make the array distinct, we must remove at least all elements 
        // up to last_dup_idx. Each operation removes 3 elements.
        // Number of operations k must satisfy 3*k > last_dup_idx.
        // k = floor(last_dup_idx / 3) + 1.
        return (last_dup_idx / 3) + 1;
    }
};
# @lc code=end