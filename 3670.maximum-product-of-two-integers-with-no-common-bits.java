# @lc app=leetcode id=3670 lang=java
#
# [3670] Maximum Product of Two Integers With No Common Bits
#

# @lc code=start
import java.util.HashMap;

class Solution {
    public long maxProduct(int[] nums) {
        HashMap<Integer, Integer> map = new HashMap<>();
        long maxProduct = 0;
        for (int num : nums) {
            int bitmask = 0, temp = num;
            // Calculate the bitmask for this number
            while (temp > 0) {
                int lowBit = temp & (-temp);
                int index = Integer.numberOfTrailingZeros(lowBit);
                bitmask |= (1 << index);
                temp -= lowBit;
            }
            // Check against all existing masks
            for (int key : map.keySet()) {
                if ((key & bitmask) == 0) { // No common set bits
                    maxProduct = Math.max(maxProduct, (long)num * map.get(key));
                }
            }
            // Store or update in map
            map.put(bitmask, Math.max(map.getOrDefault(bitmask, 0), num));
        }
        return maxProduct;
    }
}
# @lc code=end