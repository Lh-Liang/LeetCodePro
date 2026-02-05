#
# @lc app=leetcode id=3776 lang=java
#
# [3776] Minimum Moves to Balance Circular Array
#
# @lc code=start
class Solution {
    public long minMoves(int[] balance) {
        int n = balance.length;
        long total = 0;
        int negIdx = -1;
        for (int i = 0; i < n; i++) {
            total += balance[i];
            if (balance[i] < 0) negIdx = i;
        }
        if (total < 0) return -1;
        if (negIdx == -1) return 0;
        int need = -balance[negIdx];
        long moves = Long.MAX_VALUE;
        // Try only left, only right, and combinations
        for (int split = 0; split <= need; split++) {
            int[] copy = balance.clone();
            int lNeed = split;
            int rNeed = need - split;
            long cost = 0;
            int l = (negIdx - 1 + n) % n, lDist = 1;
            int r = (negIdx + 1) % n, rDist = 1;
            int lRem = lNeed, rRem = rNeed;
            boolean valid = true;
            // Left direction
            while (lRem > 0 && lDist < n) {
                int give = Math.min(copy[l], lRem);
                if (give > 0) {
                    copy[l] -= give;
                    lRem -= give;
                    cost += (long)give * lDist;
                    if (copy[l] < 0) { valid = false; break; }
                }
                l = (l - 1 + n) % n;
                lDist++;
            }
            // Right direction
            while (valid && rRem > 0 && rDist < n) {
                int give = Math.min(copy[r], rRem);
                if (give > 0) {
                    copy[r] -= give;
                    rRem -= give;
                    cost += (long)give * rDist;
                    if (copy[r] < 0) { valid = false; break; }
                }
                r = (r + 1) % n;
                rDist++;
            }
            // Explicitly verify that after transfers, all balances are non-negative
            for (int x : copy) if (x < 0) valid = false;
            if (valid && lRem == 0 && rRem == 0) {
                moves = Math.min(moves, cost);
            }
        }
        return moves == Long.MAX_VALUE ? -1 : moves;
    }
}
# @lc code=end