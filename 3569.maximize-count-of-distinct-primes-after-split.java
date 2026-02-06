#
# @lc app=leetcode id=3569 lang=java
#
# [3569] Maximize Count of Distinct Primes After Split
#
# @lc code=start
import java.util.*;
class Solution {
    private boolean[] isPrime;

    private void sieve(int max) {
        isPrime = new boolean[max + 1];
        Arrays.fill(isPrime, true);
        isPrime[0] = isPrime[1] = false;
        for (int i = 2; i * i <= max; i++) {
            if (isPrime[i]) {
                for (int j = i * i; j <= max; j += i) {
                    isPrime[j] = false;
                }
            }
        }
    }

    public int[] maximumCount(int[] nums, int[][] queries) {
        final int MAX = 100000;
        sieve(MAX);
        int n = nums.length;
        int[] result = new int[queries.length];
        for (int q = 0; q < queries.length; q++) {
            int idx = queries[q][0], val = queries[q][1];
            nums[idx] = val;
            // Build prefix and suffix sets of distinct primes
            HashSet<Integer> prefix = new HashSet<>();
            HashSet<Integer> suffix = new HashSet<>();
            int[] prefixCount = new int[n];
            int[] suffixCount = new int[n];
            // Forward: prefix distinct primes
            for (int i = 0; i < n; i++) {
                if (isPrime[nums[i]])
                    prefix.add(nums[i]);
                prefixCount[i] = prefix.size();
            }
            // Backward: suffix distinct primes
            for (int i = n - 1; i >= 0; i--) {
                if (isPrime[nums[i]])
                    suffix.add(nums[i]);
                suffixCount[i] = suffix.size();
            }
            // Try split at every k (1 <= k < n)
            int maxSum = 0;
            for (int k = 1; k < n; k++) {
                int left = prefixCount[k-1];
                int right = suffixCount[k];
                maxSum = Math.max(maxSum, left + right);
            }
            result[q] = maxSum;
        }
        return result;
    }
}
# @lc code=end