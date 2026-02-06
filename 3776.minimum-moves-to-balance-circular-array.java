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
        for (int b : balance) total += b;
        if (total < 0) return -1;
        int negIdx = -1;
        for (int i = 0; i < n; ++i) {
            if (balance[i] < 0) {
                negIdx = i;
                break;
            }
        }
        if (negIdx == -1) return 0;
        // Try both clockwise and counterclockwise
        long minMoves = Long.MAX_VALUE;
        // Clockwise
        long[] arr = new long[n];
        for (int i = 0; i < n; ++i) arr[i] = balance[i];
        long moves = 0;
        long needed = -arr[negIdx];
        int idx = (negIdx + 1) % n;
        while (needed > 0 && idx != negIdx) {
            long give = Math.min(arr[idx], needed);
            moves += give * ((idx - negIdx + n) % n);
            arr[idx] -= give;
            needed -= give;
            idx = (idx + 1) % n;
        }
        if (needed == 0) minMoves = moves;
        // Counterclockwise
        arr = new long[n];
        for (int i = 0; i < n; ++i) arr[i] = balance[i];
        moves = 0;
        needed = -arr[negIdx];
        idx = (negIdx - 1 + n) % n;
        while (needed > 0 && idx != negIdx) {
            long give = Math.min(arr[idx], needed);
            moves += give * ((negIdx - idx + n) % n);
            arr[idx] -= give;
            needed -= give;
            idx = (idx - 1 + n) % n;
        }
        if (needed == 0) minMoves = Math.min(minMoves, moves);
        return minMoves == Long.MAX_VALUE ? -1 : minMoves;
    }
}
# @lc code=end