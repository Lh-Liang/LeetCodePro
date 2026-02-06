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
        for (int i = 0; i < n; ++i) {
            int cnt = 0;
            // Try to expand to the left
            for (int l = i; l >= 0; --l) {
                int x = k - nums[l];
                boolean valid = true;
                for (int m = l; m <= i; ++m) {
                    if (nums[m] + x != k) {
                        valid = false;
                        break;
                    }
                }
                if (valid) cnt = Math.max(cnt, i - l + 1);
            }
            maxFreq = Math.max(maxFreq, cnt);
        }
        // Also count original k's
        int freqK = 0;
        for (int num : nums) if (num == k) freqK++;
        return Math.max(maxFreq, freqK);
    }
}
# @lc code=end