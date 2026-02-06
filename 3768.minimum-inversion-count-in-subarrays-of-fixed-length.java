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
        // Discretize
        int[] sorted = nums.clone();
        Arrays.sort(sorted);
        Map<Integer, Integer> valToIdx = new HashMap<>();
        int idx = 1;
        for (int v : sorted) {
            if (!valToIdx.containsKey(v)) valToIdx.put(v, idx++);
        }
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) arr[i] = valToIdx.get(nums[i]);
        int size = idx + 2;
        BIT bit = new BIT(size);
        long inv = 0;
        // First window
        for (int i = 0; i < k; i++) {
            // Count how many greater elements before i
            inv += bit.query(size - 1) - bit.query(arr[i]);
            bit.update(arr[i], 1);
        }
        long minInv = inv;
        for (int i = k; i < n; i++) {
            // Remove arr[i - k]
            bit.update(arr[i - k], -1);
            inv -= bit.query(arr[i - k] - 1);
            // Add arr[i]
            inv += bit.query(size - 1) - bit.query(arr[i]);
            bit.update(arr[i], 1);
            minInv = Math.min(minInv, inv);
        }
        return minInv;
    }
    static class BIT {
        int[] tree;
        int n;
        BIT(int n) {
            this.n = n; tree = new int[n + 2];
        }
        void update(int x, int v) {
            while (x < tree.length) { tree[x] += v; x += x & -x; }
        }
        int query(int x) {
            int sum = 0; while (x > 0) { sum += tree[x]; x -= x & -x; } return sum;
        }
    }
}
# @lc code=end