#
# @lc app=leetcode id=3420 lang=java
#
# [3420] Count Non-Decreasing Subarrays After K Operations
#

# @lc code=start
class Solution {
    public long countNonDecreasingSubarrays(int[] nums, int k) {
        int n = nums.length;
        long count = 0;
        
        // Sliding window variables
        int start = 0;
        int currentOperations = 0;
        // Auxiliary structure like a priority queue could be used here for efficiency
        
        // Iterate over each ending point of the window
        for (int end = 0; end < n; end++) {
            if (end > 0 && nums[end] < nums[end - 1]) {
                currentOperations += nums[end - 1] - nums[end];
            }
            
            while (currentOperations > k && start <= end) {
                if (start > 0 && nums[start] < nums[start - 1]) {
                    currentOperations -= nums[start - 1] - nums[start];
                }
                start++;
            }
            
            // Count all valid subarrays ending at 'end'
            count += (end - start + 1);
        }
        return count;
    }
}
# @lc code=end