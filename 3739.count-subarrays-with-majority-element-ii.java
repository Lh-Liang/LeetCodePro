#
# @lc app=leetcode id=3739 lang=java
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution {
    public long countMajoritySubarrays(int[] nums, int target) {
        int n = nums.length;
        int[] score = new int[n + 1];
        // Step 1: Build prefix scores: +1 for target, -1 for others
        for (int i = 0; i < n; ++i) {
            score[i + 1] = score[i] + (nums[i] == target ? 1 : -1);
        }
        // Step 2: Coordinate compression
        int[] sorted = score.clone();
        java.util.Arrays.sort(sorted);
        java.util.Map<Integer, Integer> compress = new java.util.HashMap<>();
        int idx = 0;
        for (int val : sorted) {
            if (!compress.containsKey(val)) {
                compress.put(val, idx++);
            }
        }
        // Step 3: Fenwick Tree (Binary Indexed Tree)
        Fenwick fenwick = new Fenwick(idx);
        long ans = 0;
        for (int i = 0; i <= n; ++i) {
            int c = compress.get(score[i]);
            // Query: sum of counts of prefix scores less than current
            ans += fenwick.query(c - 1);
            // Update: add current prefix score
            fenwick.update(c, 1);
        }
        return ans;
    }
    // Fenwick Tree implementation
    static class Fenwick {
        long[] tree;
        int n;
        Fenwick(int n) {
            this.n = n + 2;
            tree = new long[this.n];
        }
        void update(int i, long delta) {
            for (++i; i < n; i += i & -i) tree[i] += delta;
        }
        long query(int i) {
            long res = 0;
            for (++i; i > 0; i -= i & -i) res += tree[i];
            return res;
        }
    }
}
# @lc code=end