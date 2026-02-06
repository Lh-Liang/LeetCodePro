#
# @lc app=leetcode id=3779 lang=java
#
# [3779] Minimum Number of Operations to Have Distinct Elements
#
# @lc code=start
class Solution {
    public int minOperations(int[] nums) {
        if (nums.length <= 1) return 0;
        int operations = 0;
        Set<Integer> uniqueElements = new HashSet<>();
        while (true) {
            for (int i = 0; i < nums.length; i++) {
                uniqueElements.add(nums[i]);
            }
            if (uniqueElements.size() == nums.length) break; // All elements are distinct.
            operations++; // Count this operation.
            if (nums.length <= 3) break; // If fewer than three elements remain, operation ends array.
            nums = Arrays.copyOfRange(nums, 3, nums.length); // Remove first three elements.
            uniqueElements.clear(); // Reset unique tracking for new subarray.
        }
        return operations;
    }
}
# @lc code=end