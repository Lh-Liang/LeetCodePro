#
# @lc app=leetcode id=3519 lang=java
#
# [3519] Count Numbers with Non-Decreasing Digits
#
# @lc code=start
class Solution {
    static final int MOD = 1000000007;
    public int countNumbers(String l, String r, int b) {
        // Helper: Convert decimal string to base-b digit array
        int[] lDigits = toBaseB(l, b);
        int[] rDigits = toBaseB(r, b);
        int ansR = count(rDigits, b);
        int ansL = count(decOne(lDigits, b), b);
        int result = (ansR - ansL + MOD) % MOD;
        if (isNonDecreasing(lDigits)) result = (result + 1) % MOD;
        return result;
    }
    // Convert decimal string to base-b digits
    private int[] toBaseB(String num, int b) {
        java.math.BigInteger n = new java.math.BigInteger(num);
        java.util.ArrayList<Integer> digits = new java.util.ArrayList<>();
        if (n.equals(java.math.BigInteger.ZERO)) digits.add(0);
        while (n.compareTo(java.math.BigInteger.ZERO) > 0) {
            digits.add(n.mod(java.math.BigInteger.valueOf(b)).intValue());
            n = n.divide(java.math.BigInteger.valueOf(b));
        }
        int[] arr = new int[digits.size()];
        for (int i = 0; i < digits.size(); ++i) arr[arr.length - 1 - i] = digits.get(i);
        return arr;
    }
    // Decrease a base-b digit array by 1
    private int[] decOne(int[] digits, int b) {
        int n = digits.length;
        int[] res = digits.clone();
        int i = n - 1;
        while (i >= 0 && res[i] == 0) {
            res[i] = b - 1;
            i--;
        }
        if (i >= 0) res[i]--;
        // Remove leading zeros
        int start = 0;
        while (start < res.length - 1 && res[start] == 0) start++;
        int[] ans = new int[res.length - start];
        System.arraycopy(res, start, ans, 0, ans.length);
        return ans;
    }
    // DP: Count numbers <= bound (represented by digits) with non-decreasing digits
    private int count(int[] digits, int b) {
        int n = digits.length;
        Integer[][][] dp = new Integer[n + 1][b][2];
        return dfs(0, 0, true, digits, b, dp, false);
    }
    // pos: current position, prev: previous digit, tight: is current prefix tight, leadingZero: is current prefix still leading zeros
    private int dfs(int pos, int prev, boolean tight, int[] digits, int b, Integer[][][] dp, boolean leadingZero) {
        if (pos == digits.length) return leadingZero ? 0 : 1;
        int keyTight = tight ? 1 : 0;
        if (dp[pos][prev][keyTight] != null) return dp[pos][prev][keyTight];
        int res = 0;
        int limit = tight ? digits[pos] : b - 1;
        for (int d = 0; d <= limit; ++d) {
            boolean nextTight = tight && (d == limit);
            if (leadingZero && d == 0 && pos < digits.length - 1) {
                // Still leading zeros, skip counting
                res = (res + dfs(pos + 1, 0, nextTight, digits, b, dp, true)) % MOD;
            } else if (d >= prev) {
                res = (res + dfs(pos + 1, d, nextTight, digits, b, dp, false)) % MOD;
            }
        }
        dp[pos][prev][keyTight] = res;
        return res;
    }
    // Check if digits are non-decreasing
    private boolean isNonDecreasing(int[] digits) {
        for (int i = 1; i < digits.length; ++i) {
            if (digits[i] < digits[i - 1]) return false;
        }
        return true;
    }
}
# @lc code=end