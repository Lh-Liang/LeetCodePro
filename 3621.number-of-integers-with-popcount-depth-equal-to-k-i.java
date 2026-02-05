# @lc code=start
class Solution {
    public long popcountDepth(long n, int k) {
        // Precompute factorial values up to a reasonable limit for combination calculations
        long[] factorial = new long[65];
        factorial[0] = 1;
        for (int i = 1; i < 65; i++) {
            factorial[i] = factorial[i - 1] * i;
        }
        
        // Helper function to calculate combinations
        long comb(int n, int r) {
            if (r > n) return 0;
            return factorial[n] / (factorial[r] * factorial[n - r]);
        }

        // DP table where dp[i][j] represents count of numbers with length i having popcount-depth j
        long[][] dp = new long[65][k + 1];
        dp[0][0] = 1; // Base case: Only number '1' has depth 0 with length 0

        // Iterate over possible lengths up to the bit-length of n
        int maxBits = Long.toBinaryString(n).length();
        for (int bitLength = 1; bitLength <= maxBits; bitLength++) {
            for (int depth = 0; depth <= k; depth++) {
                // Calculate possible transitions from previous lengths/depths
                for (int popCount = 0; popCount < bitLength; popCount++) {
                    if (depth > 0) {
                        dp[bitLength][depth] += dp[popCount][depth - 1] * comb(bitLength - 1, popCount);
                    }
                }
            }
        }

        return dp[maxBits][k];
    }
}
# @lc code=end