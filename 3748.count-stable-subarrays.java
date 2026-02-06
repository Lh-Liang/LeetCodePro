#
# @lc app=leetcode id=3748 lang=java
#
# [3748] Count Stable Subarrays
#
# @lc code=start
class Solution {
    public long[] countStableSubarrays(int[] nums, int[][] queries) {
        int n = nums.length;
        int[] runRight = new int[n]; // runRight[i] = rightmost end of non-decreasing run starting at i
        int r = 0;
        while (r < n) {
            int l = r;
            while (r + 1 < n && nums[r] <= nums[r + 1]) r++;
            for (int i = l; i <= r; ++i) runRight[i] = r;
            r++;
        }
        // precompute number of stable subarrays ending at each position
        long[] stableEndAt = new long[n];
        int l = 0;
        while (l < n) {
            int rr = runRight[l];
            for (int i = l; i <= rr; ++i) {
                stableEndAt[i] = i - l + 1;
            }
            l = rr + 1;
        }
        // prefix sum for quick range queries
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + stableEndAt[i];
        }
        int q = queries.length;
        long[] ans = new long[q];
        for (int idx = 0; idx < q; ++idx) {
            int li = queries[idx][0], ri = queries[idx][1];
            // The answer is sum of stableEndAt[i] for i in [li, ri], but we must not count stableEndAt[i] that start before li
            // So, for each i in [li, ri], stable subarrays ending at i and starting at s >= li: count = Math.max(0, i - Math.max(li, i - stableEndAt[i] + 1) + 1)
            long total = 0;
            for (int i = li; i <= ri; ++i) {
                int start = Math.max(li, i - (int)stableEndAt[i] + 1);
                total += i - start + 1;
            }
            ans[idx] = total;
        }
        return ans;
    }
}
# @lc code=end