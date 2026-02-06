#
# @lc app=leetcode id=3739 lang=java
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution {
    public long countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;
        Map<Integer, Integer> balanceMap = new HashMap<>();
        balanceMap.put(0, 1); // Initial balance 
        int balance = 0; 
        long count = 0;
        for (int num : nums) {
            if (num == target) {
                balance++; 
            } else {
                balance--; 
            } 
            // Check if there exists a prefix with a smaller or equal balance 
            // because this means there are more targets in between 
            if (balanceMap.containsKey(balance)) {
                count += balanceMap.get(balance); 
            }
            // Add current balance state to map 
            balanceMap.put(balance, balanceMap.getOrDefault(balance, 0) + 1); 
        } 
        return count; 
    } 
}
# @lc code=end