#
# @lc app=leetcode id=3729 lang=cpp
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
class Solution {
public:
    long long numGoodSubarrays(vector<int>& nums, int k) {
        unordered_set<long long> prefixes;
        long long current_sum = 0;
        long long result = 0;
        prefixes.insert(0); // To handle subarray starting from index 0
        for (int num : nums) {
            current_sum += num;
            if (prefixes.count(current_sum % k)) {
                result++; // Found a new good subarray ending at this point
            } else {
                prefixes.insert(current_sum % k); // Record this mod result as seen
            }
        }
        return result; // Return total count of distinct good subarrays
    }
};
# @lc code=end