#
# @lc app=leetcode id=3757 lang=java
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
import java.util.*;
class Solution {
    public int countEffective(int[] nums) {
        final int MOD = 1000000007;
        int n = nums.length;
        int totalOR = 0;
        for (int num : nums) totalOR |= num;
        List<Integer> bits = new ArrayList<>();
        for (int b = 0; b < 21; ++b) if (((totalOR >> b) & 1) != 0) bits.add(b);
        int m = bits.size();
        List<List<Integer>> bitIndices = new ArrayList<>();
        for (int i = 0; i < m; ++i) bitIndices.add(new ArrayList<>());
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (((nums[i] >> bits.get(j)) & 1) != 0) bitIndices.get(j).add(i);
            }
        }
        int res = 0;
        for (int mask = 1; mask < (1 << m); ++mask) {
            Set<Integer> indices = null;
            for (int j = 0; j < m; ++j) {
                if (((mask >> j) & 1) != 0) {
                    if (indices == null) indices = new HashSet<>(bitIndices.get(j));
                    else indices.retainAll(bitIndices.get(j));
                }
            }
            if (indices == null || indices.isEmpty()) continue;
            int cnt = indices.size();
            long ways = pow(2, cnt, MOD) - 1;
            if (ways < 0) ways += MOD;
            int bitsOn = Integer.bitCount(mask);
            if ((bitsOn & 1) == 1) res = (int)((res + ways) % MOD);
            else res = (int)((res - ways + MOD) % MOD);
        }
        return res;
    }
    private long pow(long base, int exp, int mod) {
        long ans = 1;
        while (exp > 0) {
            if ((exp & 1) == 1) ans = ans * base % mod;
            base = base * base % mod;
            exp >>= 1;
        }
        return ans;
    }
}
# @lc code=end