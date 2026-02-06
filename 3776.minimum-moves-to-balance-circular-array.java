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
        long moves = 0;
        for (int i = 0; i < n; i++) {
            total += balance[i];
        }
        if (total < 0) return -1; // Impossible if total balance is negative.
        long currentBalance = 0;
        for (int i = 0; i < n; i++) {
            currentBalance += balance[i];
            moves += Math.abs(currentBalance); // Accumulate moves needed.
        }
        return moves; // Minimum moves calculated.
    }
}
# @lc code=end