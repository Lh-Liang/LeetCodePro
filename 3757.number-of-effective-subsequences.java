#
# @lc app=leetcode id=3757 lang=java
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
import java.util.*;
class Solution {
    public int countEffective(int[] nums) {
        int n = nums.length;
        final int MOD = (int)(1e9 + 7);
        int totalOR = 0;
        for (int num : nums) {
            totalOR |= num;
        }
        
        long effectiveCount = 0;
        for (int i = 0; i < n; i++) {
            if ((totalOR & ~nums[i]) != totalOR) { // Check if removing nums[i] affects the OR result
                effectiveCount += Math.pow(2, countBits(nums[i]));
                effectiveCount %= MOD;
            }
        }
        return (int)effectiveCount;
    }
    
    private int countBits(int num) {
        int count = 0;
        while (num > 0) {
            count += num & 1;
            num >>= 1;
        }
        return count;
    }
}
# @lc code=end