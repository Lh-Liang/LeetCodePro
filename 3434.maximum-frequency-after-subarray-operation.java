#
# @lc app=leetcode id=3434 lang=java
#
# [3434] Maximum Frequency After Subarray Operation
#
# @lc code=start
class Solution {
    public int maxFrequency(int[] nums, int k) {
        int n = nums.length;
        int maxFreq = 0;
        // Count number of elements already equal to k
        int kCount = 0;
        for (int num : nums) {
            if (num == k) kCount++;
        }
        // For each possible value v, try to find the longest consecutive subarray of v
        // and add k - v to all, making them k
        for (int v = 1; v <= 50; v++) {
            int left = 0, right = 0, currLen = 0, localMax = 0;
            while (right < n) {
                if (nums[right] == v) {
                    currLen++;
                    right++;
                } else {
                    localMax = Math.max(localMax, currLen);
                    // Move left to skip the first non-v element
                    right++;
                    left = right;
                    currLen = 0;
                }
            }
            localMax = Math.max(localMax, currLen);
            // The frequency if we transform a maximal block of v's to k
            int freq = localMax;
            // Add number of k's outside this block (overlap is negligible due to disjoint intervals)
            freq += kCount;
            if (v == k) freq -= localMax; // Don't double-count
            maxFreq = Math.max(maxFreq, freq);
        }
        // In case we don't do any operation, just count original k's
        maxFreq = Math.max(maxFreq, kCount);
        return maxFreq;
    }
}
# @lc code=end