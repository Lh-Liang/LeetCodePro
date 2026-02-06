#
# @lc app=leetcode id=3779 lang=java
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#
# @lc code=start
class Solution {
    public int minOperations(int[] nums) {
        int ops = 0;
        int start = 0;
        int n = nums.length;
        while (start < n) {
            // Check if current subarray is all distinct
            java.util.HashSet<Integer> set = new java.util.HashSet<>();
            boolean hasDuplicate = false;
            for (int i = start; i < n; ++i) {
                if (!set.add(nums[i])) {
                    hasDuplicate = true;
                    break;
                }
            }
            if (!hasDuplicate) return ops;
            start += 3;
            ops++;
        }
        return ops;
    }
}
# @lc code=end