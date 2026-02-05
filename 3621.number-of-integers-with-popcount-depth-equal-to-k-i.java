#
# @lc app=leetcode id=3621 lang=java
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#
# @lc code=start
class Solution {
    private int[] depthMemo = new int[100];
    
    private int popcountDepth(int x) {
        if (x == 1) return 0;
        if (depthMemo[x] != 0) return depthMemo[x];
        int next = Integer.bitCount(x);
        depthMemo[x] = 1 + popcountDepth(next);
        return depthMemo[x];
    }
    
    private long comb(int n, int k) {
        if (k < 0 || n < k) return 0;
        long res = 1;
        for (int i = 1; i <= k; i++) {
            res = res * (n - i + 1) / i;
        }
        return res;
    }
    
    private long countWithSetBits(long n, int setBits) {
        String bin = Long.toBinaryString(n);
        int len = bin.length();
        long res = 0;
        int cnt = 0;
        for (int i = 0; i < len; i++) {
            if (bin.charAt(i) == '1') {
                int rem = len - i - 1;
                res += comb(rem, setBits - cnt - 1);
                cnt++;
            }
        }
        if (cnt == setBits) res++;
        return res;
    }
    
    public long popcountDepth(long n, int k) {
        // Step 4: Explicitly handle special edge cases
        if (k == 0) return (n >= 1) ? 1 : 0; // Only x=1 qualifies if n>=1
        int maxS = 60;
        for (int i = 0; i <= maxS; i++) depthMemo[i] = 0;
        long ans = 0;
        for (int s = 1; s <= maxS; s++) {
            if (popcountDepth(s) == k - 1) {
                long cnt = countWithSetBits(n, s);
                ans += cnt;
            }
        }
        if (k == 1) ans--; // Subtract x=1 (since popcount-depth of 1 is 0)
        // Step 5: Systematically validate all special-case adjustments
        // Step 6: Ensure strict output format adherence (handled by return type here)
        return ans;
    }
}
# @lc code=end