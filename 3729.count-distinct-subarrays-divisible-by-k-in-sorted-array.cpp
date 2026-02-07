#
# @lc app=leetcode id=3729 lang=cpp
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
class Solution {
public:
    long long numGoodSubarrays(vector<int>& nums, int k) {
        unordered_map<int, int> mod_count;
        mod_count[0] = 1; // base case for a complete subarray itself being good
        int cum_sum = 0;
        int count = 0;
        for (int num : nums) {
            cum_sum += num;
            int mod_value = cum_sum % k;
            if (mod_value < 0) mod_value += k; // handle negative mods due to negative numbers or subtraction
            if (mod_count.find(mod_value) != mod_count.end()) {
                count += mod_count[mod_value]; // add the frequency of this mod value seen before
            }
            mod_count[mod_value]++; // increment the frequency of this mod value in the map
        }
        return count;
    }
};
# @lc code=end