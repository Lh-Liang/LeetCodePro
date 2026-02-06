#
# @lc app=leetcode id=3686 lang=java
#
# [3686] Number of Stable Subsequences
#

# @lc code=start
class Solution {
    public int countStableSubsequences(int[] nums) {
        final int MOD = 1_000_000_007;
        int n = nums.length;
        long oddEnd = 0, evenEnd = 0; // counts of subsequences ending in odd/even parity numbers
        long totalStable = 0; // total stable subsequences
        
        for (int num : nums) {
            if (num % 2 == 0) { // if current num is even
                evenEnd = (evenEnd + totalStable + 1) % MOD; // extend all plus itself as new start
            } else { // if current num is odd
                oddEnd = (oddEnd + totalStable + 1) % MOD; // extend all plus itself as new start
            }
            totalStable = (evenEnd + oddEnd) % MOD; // update total stable count combining both ends
        }
        return (int)totalStable; // return final count modded by MOD value to ensure size constraints met.
    }
}
# @lc code=end