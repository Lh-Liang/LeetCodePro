#
# @lc app=leetcode id=3630 lang=java
#
# [3630] Partition Array for Maximum XOR and AND
#
# @lc code=start
class Solution {
    public long maximizeXorAndXor(int[] nums) {
        int n = nums.length;
        long[] max = new long[1];
        dfs(nums, 0, 0, -1, 0, max);
        return max[0];
    }
    private void dfs(int[] nums, int idx, int xorA, int andB, int xorC, long[] max) {
        if (idx == nums.length) {
            long val = (long)xorA + ((andB == -1) ? 0 : andB) + (long)xorC;
            if (val > max[0]) max[0] = val;
            return;
        }
        // Put nums[idx] into A
        dfs(nums, idx + 1, xorA ^ nums[idx], andB, xorC, max);
        // Put nums[idx] into B
        dfs(nums, idx + 1, xorA, andB == -1 ? nums[idx] : andB & nums[idx], xorC, max);
        // Put nums[idx] into C
        dfs(nums, idx + 1, xorA, andB, xorC ^ nums[idx], max);
    }
}
# @lc code=end