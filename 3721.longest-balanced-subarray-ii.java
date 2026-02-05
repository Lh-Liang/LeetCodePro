#
# @lc app=leetcode id=3721 lang=java
#
# [3721] Longest Balanced Subarray II
#
# @lc code=start
class Solution {
    public int longestBalanced(int[] nums) {
        Map<Integer, Integer> evenMap = new HashMap<>();
        Map<Integer, Integer> oddMap = new HashMap<>();
        int maxLength = 0;
        int start = 0;

        for (int end = 0; end < nums.length; end++) {
            // Update frequency maps based on parity.
            if (nums[end] % 2 == 0) {
                evenMap.put(nums[end], evenMap.getOrDefault(nums[end], 0) + 1);
            } else {
                oddMap.put(nums[end], oddMap.getOrDefault(nums[end], 0) + 1);
            }

            // Check if current window is balanced.
            while (evenMap.size() != oddMap.size() && start <= end) {
                // Reduce frequency or remove from map to balance.
                if (nums[start] % 2 == 0) {
                    evenMap.put(nums[start], evenMap.get(nums[start]) - 1);
                    if (evenMap.get(nums[start]) == 0) {
                        evenMap.remove(nums[start]);
                    }
                } else {
                    oddMap.put(nums[start], oddMap.get(nums[start]) - 1);
                    if (oddMap.get(nums[start]) == 0) {
                        oddMap.remove(nums[start]);
                    }
                }
                start++;
            }

            // Update max length if current window is balanced.
            if (evenMap.size() == oddMap.size()) {
                maxLength = Math.max(maxLength, end - start + 1);
            }
        }

        return maxLength;
    }
}
# @lc code=end