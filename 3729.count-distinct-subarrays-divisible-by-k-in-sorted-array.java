#
# @lc app=leetcode id=3729 lang=java
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#

# @lc code=start
import java.util.*;

class Solution {
    public long numGoodSubarrays(int[] nums, int k) {
        Map<Integer, Integer> prefixSumModCount = new HashMap<>();
        prefixSumModCount.put(0, 1); // Base case for mod = 0
        long prefixSum = 0;
        long count = 0;
        for (int num : nums) {
            prefixSum += num;
            int mod = (int)(prefixSum % k);
            if (mod < 0) mod += k; // Handle negative mods
            // If this mod has been seen before, it indicates a valid subarray ending here
            count += prefixSumModCount.getOrDefault(mod, 0);
            // Increment the count of this mod in the hashmap
            prefixSumModCount.put(mod, prefixSumModCount.getOrDefault(mod, 0) + 1);
        }
        return count;
    }
}
# @lc code=end