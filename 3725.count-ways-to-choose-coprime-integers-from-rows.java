#
# @lc app=leetcode id=3725 lang=java
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
class Solution {
    public int countCoprime(int[][] mat) {
        // Constants
        final int MOD = 1000000007;
        int m = mat.length;
        int n = mat[0].length;
        
        // Dynamic programming table for counting ways
        long[] dp = new long[151]; // Possible GCD values from 1 to 150
        
        // Initialize dp array with first row elements
        for (int num : mat[0]) {
            dp[num] = 1;
        }
        
        // Iterate over each subsequent row in the matrix
        for (int i = 1; i < m; i++) {
            long[] nextDp = new long[151]; 
            for (int j = 0; j < n; j++) {
                int num = mat[i][j];
                for (int k = 1; k <= 150; k++) {
                    if (dp[k] > 0) { // Only consider non-zero counts
                        int newGCD = gcd(num, k);
                        nextDp[newGCD] = (nextDp[newGCD] + dp[k]) % MOD;
                    }
                }
            }
            dp = nextDp; // Move to next row's state as current state. 
        } 
        
        // Sum up all ways leading to a GCD of 1 combination. 
        long result = dp[1]; 
        return (int) result;
    }
    
    private int gcd(int a, int b) {
        while(b != 0){
            int temp= b;
            b=a % b;
            a=temp;
        }
        return a;
    }
}
# @lc code=end