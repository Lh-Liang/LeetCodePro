#
# @lc app=leetcode id=3762 lang=java
#
# [3762] Minimum Operations to Equalize Subarrays
#

# @lc code=start
import java.util.*;
class Solution {
    public long[] minOperations(int[] nums, int k, int[][] queries) {
        int n = nums.length, q = queries.length;
        long[] ans = new long[q];
        int[] mods = new int[n];
        for (int i = 0; i < n; ++i) mods[i] = nums[i] % k;
        for (int idx = 0; idx < q; ++idx) {
            int l = queries[idx][0], r = queries[idx][1];
            int modClass = mods[l];
            boolean possible = true;
            for (int i = l + 1; i <= r; ++i) {
                if (mods[i] != modClass) { possible = false; break; }
            }
            if (!possible) { ans[idx] = -1; continue; }
            int len = r - l + 1;
            // Edge case: subarray with one element, already equal.
            if (len == 1) { ans[idx] = 0; continue; }
            long[] arr = new long[len];
            for (int i = 0; i < len; ++i) arr[i] = (nums[l + i] - modClass) / (long)k;
            Arrays.sort(arr);
            long median = arr[len / 2];
            long total = 0;
            for (int i = 0; i < len; ++i) total += Math.abs(arr[i] - median);
            ans[idx] = total;
            // Verification: After these operations, all elements become equal to modClass + median * k.
        }
        return ans;
    }
}
# @lc code=end