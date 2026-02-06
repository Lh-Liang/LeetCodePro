class Solution {
    public long countNonDecreasingSubarrays(int[] nums, int k) {
        int n = nums.length;
        long count = 0;
        for (int start = 0; start < n; start++) {
            int operations = 0;
            for (int end = start; end < n; end++) {
                if (end > start && nums[end] < nums[end - 1]) {
                    operations += nums[end - 1] - nums[end];
                }
                if (operations <= k) {
                    count++;
                } else {
                    break; // No further subarray starting from 'start' can be valid
                }
            }
        }
        return count;
    }
}