#
# @lc app=leetcode id=3757 lang=java
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
class Solution {
    public int countEffective(int[] nums) {
        int MOD = 1000000007;
        int totalOR = 0;
        for (int num : nums) {
            totalOR |= num;
        }
        
        // Calculate effective subsequences count based on OR properties
        long result = (1L << nums.length) - 1; // Total non-empty subsequences count
        
        // Exclude non-effective subsequences by evaluating their ORs
        for (int num : nums) {
            if ((totalOR ^ num) < totalOR) { // Check if removing 'num' decreases OR strength
                result--; // Subtract ineffective ones that don't change strength
            }
        }
        return (int)(result % MOD);
    }
}
# @lc code=end