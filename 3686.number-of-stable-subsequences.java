#
# @lc app=leetcode id=3686 lang=java
#
# [3686] Number of Stable Subsequences
#
# @lc code=start
class Solution {
    public int countStableSubsequences(int[] nums) {
        final int MOD = 1000000007;
        // dp[parity][count]: #subseq ending with 'parity' and run-length 'count' (count=1 or 2)
        long[][] dp = new long[2][3];
        for (int num : nums) {
            int p = num % 2;
            int op = 1 - p;
            // new DP for this number
            long[][] ndp = new long[2][3];
            // start new subseq with this num
            ndp[p][1] = (ndp[p][1] + 1) % MOD;
            // extend existing subsequences
            for (int c = 1; c <= 2; ++c) {
                // extend subseq ending with opposite parity: reset count
                ndp[p][1] = (ndp[p][1] + dp[op][c]) % MOD;
                // extend subseq ending with same parity, if consecutive <2
                if (c < 2) {
                    ndp[p][c+1] = (ndp[p][c+1] + dp[p][c]) % MOD;
                }
            }
            dp = ndp;
        }
        long res = 0;
        for (int p = 0; p < 2; ++p)
            for (int c = 1; c <= 2; ++c)
                res = (res + dp[p][c]) % MOD;
        return (int)res;
    }
}
# @lc code=end