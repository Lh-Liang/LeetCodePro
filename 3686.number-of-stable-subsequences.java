#
# @lc app=leetcode id=3686 lang=java
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution {
    public int countStableSubsequences(int[] nums) {
        final int MOD = 1000000007;
        int n = nums.length;
        long evenEnd = 0, oddEnd = 0;
        
        for (int num : nums) {
            if (num % 2 == 0) { // num is even
                long newEvenCount = (evenEnd + 1) % MOD; // Count new sequences ending with this even
                evenEnd = (evenEnd + newEvenCount) % MOD; // Update sequences ending in even numbers
            } else { // num is odd
                long newOddCount = (oddEnd + 1) % MOD; // Count new sequences ending with this odd
                oddEnd = (oddEnd + newOddCount) % MOD; // Update sequences ending in odd numbers
            }
        }
        
        return (int)((evenEnd + oddEnd) % MOD); // Total stable subsequences modulo MOD
    }
}
# @lc code=end