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
            // Check if all remaining elements are distinct
            Set<Integer> set = new HashSet<>();
            boolean allDistinct = true;
            for (int i = start; i < n; i++) {
                if (!set.add(nums[i])) {
                    allDistinct = false;
                    break;
                }
            }
            if (allDistinct) {
                break;
            }
            // Remove up to three elements by moving start pointer
            start += Math.min(3, n - start);
            ops++;
        }
        return ops;
    }
}
# @lc code=end