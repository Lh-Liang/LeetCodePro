#
# @lc app=leetcode id=3670 lang=java
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
class Solution {
    public long maxProduct(int[] nums) {
        long maxProduct = 0;
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if ((nums[i] & nums[j]) == 0) { // No common set bits
                    maxProduct = Math.max(maxProduct, (long) nums[i] * nums[j]);
                }
            }
        }
        return maxProduct;
    }
}
# @lc code=end