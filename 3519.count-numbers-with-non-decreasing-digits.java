#
# @lc app=leetcode id=3519 lang=java
#
# [3519] Count Numbers with Non-Decreasing Digits
#
# @lc code=start
import java.math.BigInteger;
import java.util.Arrays;
import java.util.HashMap;

class Solution {
    static final int MOD = 1000000007;

    public int countNumbers(String l, String r, int b) {
        int[] digitsR = toBaseB(r, b);
        int[] digitsL = toBaseB(new BigInteger(l).subtract(BigInteger.ONE).toString(), b);
        return (int) ((count(digitsR, b) - count(digitsL, b) + MOD) % MOD);
    }

    private int[] toBaseB(String num, int b) {
        BigInteger n = new BigInteger(num);
        if (n.equals(BigInteger.ZERO)) return new int[]{0};
        int[] tmp = new int[105];
        int idx = tmp.length - 1;
        while (n.compareTo(BigInteger.ZERO) > 0) {
            BigInteger[] dr = n.divideAndRemainder(BigInteger.valueOf(b));
            tmp[idx--] = dr[1].intValue();
            n = dr[0];
        }
        int[] res = Arrays.copyOfRange(tmp, idx+1, tmp.length);
        return res;
    }

    private long count(int[] digits, int b) {
        int n = digits.length;
        Long[][][][] memo = new Long[n+1][b+1][2][2];
        return dp(0, 0, true, false, digits, b, memo);
    }

    // pos: current digit
    // prev: previous digit (0~b-1), or 0 when not started
    // tight: whether we are still tight to the bound
    // started: whether we've placed any nonzero digit yet
    private long dp(int pos, int prev, boolean tight, boolean started, int[] digits, int b, Long[][][][] memo) {
        if (pos == digits.length) return started ? 1 : 0;
        int tightLim = tight ? digits[pos] : b-1;
        int minDigit = started ? prev : 0;
        if (memo[pos][prev][tight?1:0][started?1:0] != null)
            return memo[pos][prev][tight?1:0][started?1:0];
        long res = 0;
        for (int d = minDigit; d <= tightLim; d++) {
            boolean nextTight = tight && (d == tightLim);
            boolean nextStarted = started || (d != 0);
            res = (res + dp(pos+1, nextStarted ? d : 0, nextTight, nextStarted, digits, b, memo)) % MOD;
        }
        // If not started, we can skip leading zeros
        if (!started) {
            // Only skip if not at last digit
            if (pos < digits.length - 1)
                res = (res + dp(pos+1, 0, tight && (0 == tightLim), false, digits, b, memo)) % MOD;
        }
        memo[pos][prev][tight?1:0][started?1:0] = res;
        return res;
    }
}
# @lc code=end