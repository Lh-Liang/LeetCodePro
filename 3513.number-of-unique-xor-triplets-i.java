#
# @lc app=leetcode id=3513 lang=java
#
# [3513] Number of Unique XOR Triplets I
#
# @lc code=start
class Solution {
    public int uniqueXorTriplets(int[] nums) {
        Set<Integer> uniqueXorValues = new HashSet<>();
        int n = nums.length;
        int[] prefixXor = new int[n + 1];
        for (int i = 0; i < n; i++) {
            prefixXor[i + 1] = prefixXor[i] ^ nums[i];
        }
        for (int i = 0; i < n; i++) {
            for (int j = i; j < n; j++) {
                uniqueXorValues.add(prefixXor[j + 1] ^ prefixXor[i]);
            }
        }
        return uniqueXorValues.size();
    }
}
# @lc code=end