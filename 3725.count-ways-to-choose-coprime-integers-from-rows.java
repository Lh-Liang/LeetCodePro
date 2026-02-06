#
# @lc app=leetcode id=3725 lang=java
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
import java.util.*;
class Solution {
    public int countCoprime(int[][] mat) {
        int MOD = 1_000_000_007;
        int m = mat.length, n = mat[0].length;
        Map<Integer, Integer> dp = new HashMap<>();
        // Initialize DP with first row
        for (int val : mat[0]) {
            dp.put(val, dp.getOrDefault(val, 0) + 1);
        }
        // Process each row
        for (int i = 1; i < m; ++i) {
            Map<Integer, Integer> next = new HashMap<>();
            for (int val : mat[i]) {
                for (Map.Entry<Integer, Integer> entry : dp.entrySet()) {
                    int newGcd = gcd(val, entry.getKey());
                    next.put(newGcd, (int)(((long)next.getOrDefault(newGcd, 0) + entry.getValue()) % MOD));
                }
                // Also start new sequences from this row
                next.put(val, (int)(((long)next.getOrDefault(val, 0) + 1) % MOD));
            }
            dp = next;
        }
        return dp.getOrDefault(1, 0);
    }
    private int gcd(int a, int b) {
        while (b != 0) { int t = b; b = a % b; a = t; }
        return a;
    }
}
# @lc code=end