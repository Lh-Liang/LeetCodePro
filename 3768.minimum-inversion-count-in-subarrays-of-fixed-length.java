#
# @lc app=leetcode id=3768 lang=java
#
# [3768] Minimum Inversion Count in Subarrays of Fixed Length
#
# @lc code=start
import java.util.*;
class Solution {
    public long minInversionCount(int[] nums, int k) {
        int n = nums.length;
        int[] copy = Arrays.copyOf(nums, n);
        Arrays.sort(copy);
        Map<Integer, Integer> rank = new HashMap<>();
        int idx = 1;
        for (int num : copy) {
            if (!rank.containsKey(num)) rank.put(num, idx++);
        }
        int[] compressed = new int[n];
        for (int i = 0; i < n; ++i) {
            compressed[i] = rank.get(nums[i]);
        }
        int maxVal = idx;
        BIT bit = new BIT(maxVal + 2);
        long inv = 0;
        for (int i = 0; i < k; ++i) {
            inv += bit.query(maxVal) - bit.query(compressed[i]);
            bit.update(compressed[i], 1);
        }
        long res = inv;
        for (int i = k; i < n; ++i) {
            // Remove nums[i-k]
            bit.update(compressed[i - k], -1);
            inv -= bit.query(compressed[i - k] - 1);
            // Add nums[i]
            inv += bit.query(maxVal) - bit.query(compressed[i]);
            bit.update(compressed[i], 1);
            res = Math.min(res, inv);
        }
        return res;
    }
    // BIT supporting prefix sums
    class BIT {
        int[] tree; int n;
        BIT(int n) { this.n = n; tree = new int[n+2]; }
        void update(int i, int v) { while (i < tree.length) { tree[i] += v; i += i & -i; } }
        int query(int i) { int s = 0; while (i > 0) { s += tree[i]; i -= i & -i; } return s; }
    }
}
# @lc code=end