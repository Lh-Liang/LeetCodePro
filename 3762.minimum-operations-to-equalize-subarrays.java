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
        // Precompute nums[i] % k for feasibility
        int[] mods = new int[n];
        for (int i = 0; i < n; ++i) {
            mods[i] = nums[i] % k;
        }
        // Precompute prefix sums for each value of mods
        Map<Integer, int[]> modPrefix = new HashMap<>();
        for (int m = 0; m < k; ++m) {
            modPrefix.put(m, new int[n+1]);
        }
        for (int i = 0; i < n; ++i) {
            for (int m = 0; m < k; ++m) {
                modPrefix.get(m)[i+1] = modPrefix.get(m)[i] + (mods[i]==m ? 1 : 0);
            }
        }
        for (int idx = 0; idx < q; ++idx) {
            int l = queries[idx][0], r = queries[idx][1];
            int baseMod = mods[l];
            // Check all mods are the same
            int modCount = modPrefix.get(baseMod)[r+1] - modPrefix.get(baseMod)[l];
            if (modCount != (r-l+1)) {
                ans[idx] = -1;
                continue;
            }
            // Transform to (nums[i] - base) / k
            List<Integer> transformed = new ArrayList<>();
            for (int i = l; i <= r; ++i) {
                transformed.add((nums[i] - baseMod) / k);
            }
            Collections.sort(transformed);
            int m = transformed.size();
            int median = transformed.get(m/2);
            long sum = 0;
            for (int v : transformed) {
                sum += Math.abs(v - median);
            }
            ans[idx] = sum;
        }
        return ans;
    }
}
# @lc code=end