#
# @lc app=leetcode id=3757 lang=java
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
class Solution {
    public int countEffective(int[] nums) {
        int n = nums.length;
        final int MOD = 1_000_000_007;
        int totalOr = 0;
        for (int x : nums) totalOr |= x;

        // Find all set bits in totalOr
        List<Integer> bits = new ArrayList<>();
        for (int b = 0; b < 22; ++b)
            if (((totalOr >> b) & 1) == 1)
                bits.add(b);
        int k = bits.size();
        int[][] bitContrib = new int[k][];
        // For each bit, collect indices of contributors
        for (int i = 0; i < k; ++i) {
            int b = bits.get(i);
            List<Integer> indices = new ArrayList<>();
            for (int j = 0; j < n; ++j) if (((nums[j] >> b) & 1) == 1) indices.add(j);
            bitContrib[i] = indices.stream().mapToInt(e -> e).toArray();
        }
        int[] pow2 = new int[n+1];
        pow2[0] = 1;
        for (int i = 1; i <= n; ++i) pow2[i] = (int)((pow2[i-1]*2L)%MOD);
        int res = 0;
        // Inclusion-exclusion over non-empty bit subsets
        for (int mask = 1; mask < (1<<k); ++mask) {
            Set<Integer> toRemove = new HashSet<>();
            for (int b = 0; b < k; ++b) {
                if (((mask>>b)&1)==1) {
                    for (int idx : bitContrib[b]) toRemove.add(idx);
                }
            }
            int m = toRemove.size();
            int ways = (int)((pow2[m]-1L+MOD)%MOD * (long)pow2[n-m]%MOD);
            // Inclusion-Exclusion: add if odd number of bits, subtract if even
            if (Integer.bitCount(mask)%2==1)
                res = (res + ways) % MOD;
            else
                res = (res - ways + MOD) % MOD;
        }
        return res;
    }
}
# @lc code=end