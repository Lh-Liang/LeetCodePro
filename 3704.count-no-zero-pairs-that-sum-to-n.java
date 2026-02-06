#
# @lc app=leetcode id=3704 lang=java
#
# [3704] Count No-Zero Pairs That Sum to N
#
# @lc code=start
class Solution {
    public long countNoZeroPairs(long n) {
        String s = Long.toString(n);
        int len = s.length();
        Long[][][][] memo = new Long[len + 1][2][2][2];
        return dfs(0, 1, 1, 0, s, memo);
    }
    // pos: current digit pos, tightA, tightB, carry
    private long dfs(int pos, int tightA, int tightB, int carry, String s, Long[][][][] memo) {
        if (pos == s.length()) {
            return carry == 0 ? 1 : 0;
        }
        if (memo[pos][tightA][tightB][carry] != null) {
            return memo[pos][tightA][tightB][carry];
        }
        long res = 0;
        int dig = s.charAt(pos) - '0';
        for (int da = 1; da <= 9; da++) {
            for (int db = 1; db <= 9; db++) {
                int sum = da + db + carry;
                if (sum % 10 != dig) continue;
                int nc = sum / 10;
                int ntightA = tightA == 1 && da == dig ? 1 : 0;
                int ntightB = tightB == 1 && db == dig ? 1 : 0;
                if (tightA == 1 && da > dig) continue;
                if (tightB == 1 && db > dig) continue;
                res += dfs(pos + 1, ntightA, ntightB, nc, s, memo);
            }
        }
        memo[pos][tightA][tightB][carry] = res;
        return res;
    }
}
# @lc code=end