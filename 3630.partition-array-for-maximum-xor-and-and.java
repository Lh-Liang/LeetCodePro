/*
 * @lc app=leetcode id=3630 lang=java
 *
 * [3630] Partition Array for Maximum XOR and AND
 */

// @lc code=start
class Solution {
    public long maximizeXorAndXor(int[] nums) {
        long[] max = new long[1];
        dfs(nums, 0, 0, false, 0, false, 0, false, max);
        return max[0];
    }
    // xorA, hasA: current XOR and non-empty flag for group A
    // andB, hasB: current AND and non-empty flag for group B
    // xorC, hasC: current XOR and non-empty flag for group C
    private void dfs(int[] nums, int idx, int xorA, boolean hasA, int andB, boolean hasB, int xorC, boolean hasC, long[] max) {
        if (idx == nums.length) {
            long andBValue = hasB ? andB : 0;
            long sum = (hasA ? xorA : 0) + andBValue + (hasC ? xorC : 0);
            if (sum > max[0]) max[0] = sum;
            return;
        }
        int num = nums[idx];
        // Assign to A
        dfs(nums, idx + 1, xorA ^ num, true, andB, hasB, xorC, hasC, max);
        // Assign to B
        if (!hasB) {
            dfs(nums, idx + 1, xorA, hasA, num, true, xorC, hasC, max);
        } else {
            dfs(nums, idx + 1, xorA, hasA, andB & num, true, xorC, hasC, max);
        }
        // Assign to C
        dfs(nums, idx + 1, xorA, hasA, andB, hasB, xorC ^ num, true, max);
    }
}
// @lc code=end