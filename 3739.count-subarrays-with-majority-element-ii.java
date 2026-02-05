#
# @lc app=leetcode id=3739 lang=java
#
# [3739] Count Subarrays With Majority Element II
#

# @lc code=start
class Solution {
    public long countMajoritySubarrays(int[] nums, int target) {
        // Transform nums into +1/-1 based on target
        int n = nums.length;
        int[] arr = new int[n];
        for (int i = 0; i < n; ++i) {
            arr[i] = (nums[i] == target ? 1 : -1);
        }
        // Calculate prefix sums
        int[] prefix = new int[n+1];
        for (int i = 0; i < n; ++i) {
            prefix[i+1] = prefix[i] + arr[i];
        }
        // To handle negative prefix sums, compress the prefix sums
        java.util.TreeSet<Integer> set = new java.util.TreeSet<>();
        for (int x : prefix) set.add(x);
        java.util.HashMap<Integer, Integer> idxMap = new java.util.HashMap<>();
        int idx = 0;
        for (int x : set) idxMap.put(x, idx++);
        // Fenwick Tree (BIT) for prefix sum frequencies
        class BIT {
            private long[] bit;
            public BIT(int n) { bit = new long[n+2]; }
            public void add(int i, long v) { for (++i; i < bit.length; i += i & -i) bit[i] += v; }
            public long sum(int i) { long res = 0; for (++i; i > 0; i -= i & -i) res += bit[i]; return res; }
        }
        BIT bit = new BIT(idx);
        long result = 0;
        // For each prefix sum, count number of previous prefix sums less than current
        for (int i = 0; i <= n; ++i) {
            int mapped = idxMap.get(prefix[i]);
            if (i > 0) {
                result += bit.sum(mapped - 1);
            }
            bit.add(mapped, 1);
        }
        return result;
    }
}
# @lc code=end