#
# @lc app=leetcode id=3470 lang=java
#
# [3470] Permutations IV
#

# @lc code=start
import java.util.*;
class Solution {
    public int[] permute(int n, long k) {
        // Precompute the list of odds and evens
        List<Integer> odds = new ArrayList<>();
        List<Integer> evens = new ArrayList<>();
        for (int i = 1; i <= n; ++i) {
            if (i % 2 == 1) odds.add(i);
            else evens.add(i);
        }
        int totalOdds = odds.size(), totalEvens = evens.size();
        // Memoization map: key = odd_left * 101 + even_left * 2 + parity
        Map<Long, Long> dp = new HashMap<>();
        // Count valid alternatings for given left counts and last parity
        java.util.function.BiFunction<Integer, Integer, Long> countStarts = (oddsLeft, evensLeft) -> {
            // Try both parity starts (if possible)
            long res = 0;
            if (oddsLeft > 0) res += countDP(oddsLeft - 1, evensLeft, 1, dp);
            if (evensLeft > 0) res += countDP(oddsLeft, evensLeft - 1, 0, dp);
            return res;
        };
        // Compute total valid perms
        long total = countStarts.apply(totalOdds, totalEvens);
        if (k > total) return new int[0];
        // Used flags
        boolean[] used = new boolean[n + 1];
        int[] ans = new int[n];
        int idx = 0;
        int oddLeft = totalOdds, evenLeft = totalEvens;
        int lastParity = -1; // -1 means no previous
        while (idx < n) {
            for (int i = 1; i <= n; ++i) {
                if (used[i]) continue;
                int p = i % 2;
                // If first pos, can pick any
                if (lastParity == -1 || p != lastParity) {
                    int newOdd = oddLeft, newEven = evenLeft;
                    if (p == 1) newOdd--; else newEven--;
                    if (newOdd < 0 || newEven < 0) continue;
                    long cnt = countDP(newOdd, newEven, p, dp);
                    if (k > cnt) {
                        k -= cnt;
                    } else {
                        ans[idx++] = i;
                        used[i] = true;
                        oddLeft = newOdd;
                        evenLeft = newEven;
                        lastParity = p;
                        break;
                    }
                }
            }
        }
        return ans;
    }
    // DP: ways to fill with odd_left, even_left, last_parity (0 = even, 1 = odd)
    private long countDP(int odd, int even, int last, Map<Long, Long> dp) {
        if (odd == 0 && even == 0) return 1;
        long key = ((long)odd) * 101 * 2 + ((long)even) * 2 + last;
        if (dp.containsKey(key)) return dp.get(key);
        long res = 0;
        if (last == 0 && odd > 0) {
            res += countDP(odd - 1, even, 1, dp);
        } else if (last == 1 && even > 0) {
            res += countDP(odd, even - 1, 0, dp);
        }
        dp.put(key, res);
        return res;
    }
}
# @lc code=end