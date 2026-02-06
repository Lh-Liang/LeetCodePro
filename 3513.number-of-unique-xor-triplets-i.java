#
# @lc app=leetcode id=3513 lang=java
#
# [3513] Number of Unique XOR Triplets I
#
# @lc code=start
class Solution {
    public int uniqueXorTriplets(int[] nums) {
        Set<Integer> xorSet = new HashSet<>();
        int n = nums.length;
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                for (int k = j; k < n; k++) {
                    xorSet.add(nums[i] ^ nums[j] ^ nums[k]);
                }
            }
        }
        return xorSet.size();
    }
}
# @lc code=end