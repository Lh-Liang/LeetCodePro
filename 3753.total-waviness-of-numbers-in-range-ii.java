#
# @lc app=leetcode id=3753 lang=java
#
# [3753] Total Waviness of Numbers in Range II
#
# @lc code=start
import java.util.*;
class Solution {
    public long totalWaviness(long num1, long num2) {
        return countWaviness(num2) - countWaviness(num1 - 1);
    }
    private long countWaviness(long n) {
        if (n < 100) return 0;
        char[] digits = Long.toString(n).toCharArray();
        // dp[pos][tight][prev][prev2][leadZero] = long
        Long[][][][][] memo = new Long[digits.length + 1][2][11][11][2];
        return dfs(0, 1, 10, 10, 1, digits, memo);
    }
    // pos: current digit position, tight: bound flag, prev1: previous digit, prev2: digit before prev1, leadZero: leading zero flag
    private long dfs(int pos, int tight, int prev1, int prev2, int leadZero, char[] digits, Long[][][][][] memo) {
        if (pos == digits.length) return 0;
        if (memo[pos][tight][prev1][prev2][leadZero] != null) return memo[pos][tight][prev1][prev2][leadZero];
        int limit = tight == 1 ? digits[pos] - '0' : 9;
        long res = 0;
        for (int d = 0; d <= limit; ++d) {
            int newTight = (tight == 1 && d == limit) ? 1 : 0;
            int newLeadZero = (leadZero == 1 && d == 0) ? 1 : 0;
            int newPrev1 = (newLeadZero == 1) ? 10 : d;
            long add = 0;
            if (pos >=2 && leadZero == 0) {
                // prev2 and prev1 are valid
                if (prev1 > prev2 && prev1 > d) add = 1;
                if (prev1 < prev2 && prev1 < d) add = 1;
            }
            res += dfs(pos+1, newTight, newPrev1, prev1, newLeadZero, digits, memo) + add;
        }
        memo[pos][tight][prev1][prev2][leadZero] = res;
        return res;
    }
}
# @lc code=end