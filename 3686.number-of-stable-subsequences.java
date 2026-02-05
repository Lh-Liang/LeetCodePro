#
# @lc app=leetcode id=3686 lang=java
#
# [3686] Number of Stable Subsequences
#
# @lc code=start
class Solution {
    public int countStableSubsequences(int[] nums) {
        int n = nums.length;
        int MOD = 1000000007;
        // dp[i][c][p]: number of stable subsequences using first i elements,
        // ending with c consecutive p parity elements (c=0: no last elem, 1 or 2), p=0: even, 1: odd
        // To optimize, we only need 2 dp arrays (prev, curr), since state at i only depends on i-1
        int[][][] dp = new int[2][3][2];
        dp[0][0][0] = 1; // empty subsequence, parity doesn't matter
        dp[0][0][1] = 1;
        for(int i = 0; i < n; ++i) {
            int curr = (i+1)%2, prev = i%2;
            // reset curr layer
            for(int c=0; c<=2; ++c) for(int p=0; p<=1; ++p) dp[curr][c][p]=0;
            int parity = nums[i]%2;
            // For all previous states
            for(int c=0; c<=2; ++c) {
                for(int p=0; p<=1; ++p) {
                    int val = dp[prev][c][p];
                    if(val==0) continue;
                    // Option 1: skip nums[i] (don't take)
                    dp[curr][c][p] = (dp[curr][c][p] + val)%MOD;
                    // Option 2: take nums[i]
                    if(c==0) {
                        // Start a new subsequence
                        dp[curr][1][parity] = (dp[curr][1][parity] + val)%MOD;
                    } else {
                        if(parity==p) {
                            if(c<2) {
                                dp[curr][c+1][p] = (dp[curr][c+1][p] + val)%MOD;
                            } // else: would make three consecutive, skip
                        } else {
                            // reset count
                            dp[curr][1][parity] = (dp[curr][1][parity] + val)%MOD;
                        }
                    }
                }
            }
        }
        int ans = 0;
        int last = n%2;
        // Sum all non-empty subsequences
        for(int c=1; c<=2; ++c) for(int p=0; p<=1; ++p) ans = (ans + dp[last][c][p])%MOD;
        return ans;
    }
}
# @lc code=end