#
# @lc app=leetcode id=3748 lang=java
#
# [3748] Count Stable Subarrays
#
# @lc code=start
class Solution {
    public long[] countStableSubarrays(int[] nums, int[][] queries) {
        int n = nums.length;
        long[] result = new long[queries.length];
        
        // Process each query individually.
        for (int q = 0; q < queries.length; q++) {
            int li = queries[q][0];
            int ri = queries[q][1];
            long count = 0;
            
            // Use two pointers to find stable subarrays within [li, ri]
            int start = li;
            while (start <= ri) {
                int end = start;
                while (end <= ri && (end == start || nums[end - 1] <= nums[end])) {
                    end++;
                }
                // Calculate number of subarrays in this stable segment
                int length = end - start;
                count += ((long)length * (length + 1)) / 2; // Sum of first 'length' natural numbers
                start = end; // Move start to where instability was found or end of range
            }
            result[q] = count;
        }
        return result;
    }
}
# @lc code=end