#
# @lc app=leetcode id=3670 lang=java
#
# [3670] Maximum Product of Two Integers With No Common Bits
#
# @lc code=start
class Solution {
    public long maxProduct(int[] nums) {
        // Map from bitmask to maximum number with that bitmask
        java.util.Map<Integer, Integer> maskToMax = new java.util.HashMap<>();
        for (int num : nums) {
            int mask = num;
            maskToMax.put(mask, Math.max(maskToMax.getOrDefault(mask, 0), num));
        }
        long maxProduct = 0;
        Integer[] masks = maskToMax.keySet().toArray(new Integer[0]);
        int n = masks.length;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if ((masks[i] & masks[j]) == 0) {
                    long prod = (long)maskToMax.get(masks[i]) * maskToMax.get(masks[j]);
                    if (prod > maxProduct) maxProduct = prod;
                }
            }
        }
        return maxProduct;
    }
}
# @lc code=end