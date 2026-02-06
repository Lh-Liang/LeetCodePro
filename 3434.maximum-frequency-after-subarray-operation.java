#
# @lc app=leetcode id=3434 lang=java
#
# [3434] Maximum Frequency After Subarray Operation
#
# @lc code=start
class Solution {
    public int maxFrequency(int[] nums, int k) {
        int left = 0, right = 0, maxFreq = 0;
        int currentSum = 0;
        Arrays.sort(nums); // Sorting helps maintain order for frequency evaluation.
        while (right < nums.length) {
            currentSum += nums[right];
            // Check if current window is valid by comparing with the cost of converting all elements to nums[right].
            while ((right - left + 1) * nums[right] - currentSum > k) {
                currentSum -= nums[left]; // Adjust by removing elements from left.
                left++; // Shrink window from the left if it exceeds allowed operations (k).
            }
            maxFreq = Math.max(maxFreq, right - left + 1); // Update maximum frequency found.
            right++; // Expand window by moving right pointer forward.
        }
        return maxFreq; // Return the maximum frequency of k possible after one operation.
    }
}
# @lc code=end