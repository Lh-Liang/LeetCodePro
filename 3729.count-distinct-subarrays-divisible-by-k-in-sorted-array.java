#
# @lc app=leetcode id=3729 lang=java
#
# [3729] Count Distinct Subarrays Divisible by K in Sorted Array
#
# @lc code=start
import java.util.*;
class Solution {
    public long numGoodSubarrays(int[] nums, int k) {
        int n = nums.length;
        long[] prefixSum = new long[n + 1];
        for (int i = 0; i < n; ++i) {
            prefixSum[i + 1] = prefixSum[i] + nums[i];
        }
        // Rolling hash parameters
        long base = 1000003L, mod = (long)1e18 + 3;
        long[] pow = new long[n + 1];
        pow[0] = 1;
        for (int i = 1; i <= n; ++i) pow[i] = (pow[i - 1] * base) % mod;
        long[] hash = new long[n + 1];
        for (int i = 0; i < n; ++i) {
            hash[i + 1] = (hash[i] * base + nums[i]) % mod;
        }
        Set<Long> seen = new HashSet<>();
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j <= n; ++j) {
                long sum = prefixSum[j] - prefixSum[i];
                if (sum % k == 0) {
                    long h = (hash[j] - hash[i] * pow[j - i] % mod + mod) % mod;
                    seen.add(h);
                }
            }
        }
        return seen.size();
    }
}
# @lc code=end