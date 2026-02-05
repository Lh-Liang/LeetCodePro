# @lc code=start
class Solution {
    public int maxFrequency(int[] nums, int k) {
        Arrays.sort(nums);
        int left = 0, maxFreq = 0;
        long total = 0;
        for (int right = 0; right < nums.length; right++) {
            total += nums[right];
            // Check if current window is valid
            while ((long)(right - left + 1) * nums[right] - total > k) {
                total -= nums[left];
                left++;
            }
            // Update max frequency found
            maxFreq = Math.max(maxFreq, right - left + 1);
        }
        return maxFreq;
    }
}
# @lc code=end