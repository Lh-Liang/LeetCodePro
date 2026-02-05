#
# @lc app=leetcode id=3753 lang=java
#
# [3753] Total Waviness of Numbers in Range II
#
# @lc code=start
class Solution {
    public long totalWaviness(long num1, long num2) {
        return countWaviness(num2) - countWaviness(num1 - 1);
    }

    private long countWaviness(long n) {
        char[] digits = Long.toString(n).toCharArray();
        int len = digits.length;
        // dp[pos][prev][pprev][tight][started] = waviness sum
        Long[][][][][] memo = new Long[len + 1][11][11][2][2];
        return dfs(0, 10, 10, 1, 0, digits, memo);
    }

    // pos: current index, prev: previous digit, pprev: pre-previous digit
    private long dfs(int pos, int prev, int pprev, int tight, int started, char[] digits, Long[][][][][] memo) {
        if (pos == digits.length) return 0;
        if (memo[pos][prev][pprev][tight][started] != null) return memo[pos][prev][pprev][tight][started];
        long res = 0;
        int limit = tight == 1 ? digits[pos] - '0' : 9;
        for (int d = 0; d <= limit; ++d) {
            int nTight = (tight == 1 && d == limit) ? 1 : 0;
            int nStarted = (started == 1 || d != 0) ? 1 : 0;
            int wave = 0;
            if (nStarted == 1 && pos >= 2) {
                if (prev > pprev && prev > d) wave = 1; // peak
                if (prev < pprev && prev < d) wave = 1; // valley
            }
            res += wave + dfs(pos + 1, d, prev, nTight, nStarted, digits, memo);
        }
        return memo[pos][prev][pprev][tight][started] = res;
    }
}
# @lc code=end