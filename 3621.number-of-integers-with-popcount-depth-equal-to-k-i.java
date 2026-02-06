#
# @lc app=leetcode id=3621 lang=java
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#
# @lc code=start
class Solution {
    // Precompute popcount-depth for numbers up to 60 (since 10^15 < 2^50)
    private int[] depth = new int[65];
    private void initPopcountDepth() {
        depth[0] = -1; // 0 is not valid for our problem
        depth[1] = 0;
        for (int i = 2; i < depth.length; i++) {
            int cnt = 0, x = i;
            while (x != 1) {
                x = Integer.bitCount(x);
                cnt++;
            }
            depth[i] = cnt;
        }
    }

    // Count how many numbers <= n have exactly s set bits
    private long count(long n, int s) {
        if (s == 0) return 1;
        int bits = 0; long temp = n;
        int[] pos = new int[65];
        while (temp > 0) {
            pos[bits++] = (int)(temp & 1);
            temp >>= 1;
        }
        long res = 0; int ones = 0;
        for (int i = bits - 1; i >= 0; i--) {
            if (pos[i] == 1) {
                res += comb(i, s - ones);
            }
            if (pos[i] == 1) ones++;
            if (ones > s) break;
        }
        if (ones == s) res += 1;
        return res;
    }

    // Compute n choose k
    private long comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        long res = 1;
        for (int i = 1; i <= k; i++) {
            res = res * (n - i + 1) / i;
        }
        return res;
    }

    public long popcountDepth(long n, int k) {
        if (k == 0) return n == 1 ? 1 : 0;
        initPopcountDepth();
        long ans = 0;
        for (int i = 1; i < depth.length; i++) {
            if (depth[i] == k - 1) { // popcount-depth is k (k-1 steps to get to 1)
                ans += count(n, i);
            }
        }
        return ans;
    }
}
# @lc code=end