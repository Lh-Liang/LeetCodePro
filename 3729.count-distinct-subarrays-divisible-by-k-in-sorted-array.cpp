#
# @lc app=leetcode id=3729 lang=cpp
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
class Solution {
public:
    long long numGoodSubarrays(vector<int>& nums, int k) {
        unordered_map<int, int> modCount;
        unordered_set<string> uniqueSubarrays;
        int prefixSum = 0;
        long long count = 0;
        modCount[0] = 1; // Initial condition for subarray starting from index 0
        string currentSeq = "";
        for (int num : nums) {
            currentSeq += to_string(num) + ",";
            prefixSum += num;
            int mod = prefixSum % k;
            if (mod < 0) mod += k; // Normalize negative mods to positive equivalents
            if (modCount.count(mod)) {
                // Check if this sequence is already counted
                if (uniqueSubarrays.find(currentSeq) == uniqueSubarrays.end()) {
                    count += modCount[mod];
                    uniqueSubarrays.insert(currentSeq);
                }
            }
            modCount[mod]++;
        }
        return count;
    }
};
# @lc code=end