#
# @lc app=leetcode id=3434 lang=cpp
#
# [3434] Maximum Frequency After Subarray Operation
#

# @lc code=start
class Solution {
public:
    int maxFrequency(vector<int>& nums, int k) {
        int n = nums.size();
        int max_freq = 0;
        // For each possible subarray, try to convert all to k by the same x
        // Since value ranges are small, for each position, build prefix sum where nums[i] == k
        // We can also try for each possible start position, expand window where nums[i..j] can all be shifted to k by the same x
        // But since only one operation is allowed, for each window, count how many elements can be made k
        // For each possible window, check how many elements can be converted to k
        for (int i = 0; i < n; ++i) {
            int freq = 0;
            for (int j = i; j < n; ++j) {
                // x to make nums[i..j] all k is k - nums[j]
                // All elements in nums[i..j] must be transformed to k by adding x = k - nums[m] (for each m)
                // But since x can be any integer, we can always pick x = k - nums[m] for any m in i..j
                // So, for this window, after operation, nums[i..j] become k
                // Frequency is (j-i+1) + count of k's outside this window
                int outside_k = 0;
                for (int m = 0; m < i; ++m) if (nums[m] == k) outside_k++;
                for (int m = j+1; m < n; ++m) if (nums[m] == k) outside_k++;
                int total = (j-i+1) + outside_k;
                max_freq = max(max_freq, total);
            }
        }
        return max_freq;
    }
};
# @lc code=end