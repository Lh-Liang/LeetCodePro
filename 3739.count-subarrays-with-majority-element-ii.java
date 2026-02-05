#
# @lc app=leetcode id=3739 lang=java
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution {
    public long countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;
        long count = 0L;
        Map<Integer, Integer> balanceMap = new HashMap<>();
        balanceMap.put(0, 1); // initial balance 0 appears once
        int balance = 0;
        for (int num : nums) {
            if (num == target) {
                balance++;
            } else {
                balance--;
            }
            // Check if there's a previous subarray that makes this current subarray valid.
            count += balanceMap.getOrDefault(balance - 1, 0);
            balanceMap.put(balance, balanceMap.getOrDefault(balance, 0) + 1);
        }
        return count;
    }
}
# @lc code=end