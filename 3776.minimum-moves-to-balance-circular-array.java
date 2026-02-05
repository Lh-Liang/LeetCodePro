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
        int negIndex = -1;
        
        // Calculate total balance and find initial negative index
        for (int i = 0; i < n; i++) {
            total += balance[i];
            if (balance[i] < 0) negIndex = i;
        }
        
        if (total < 0) return -1; // Impossible to balance if total is negative
        
        int posIndex = 0;
        long moves = 0;
        
        while (negIndex != -1) {
            while (balance[posIndex] <= 0) posIndex = (posIndex + 1) % n; // Find next positive index
            
            while (balance[negIndex] < 0 && balance[posIndex] > 0) {
                balance[negIndex]++;
                balance[posIndex]--;
                moves++;
                if (balance[negIndex] == 0) {
                    negIndex = -1; // Reset as no more negative balances
                    for (int i = (negIndex + 1) % n; i != posIndex; i = (i + 1) % n) {
                        if (balance[i] < 0) {
                            negIndex = i;
                            break;
                        }
                    }
                }
            }
            posIndex = (posIndex + 1) % n; // Move to next positive index
        }
        return moves;
    }
}
# @lc code=end