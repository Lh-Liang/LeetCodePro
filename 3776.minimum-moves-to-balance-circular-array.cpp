#
# @lc app=leetcode id=3776 lang=cpp
#
# [3776] Minimum Moves to Balance Circular Array
#
# @lc code=start
class Solution {
public:
    long long minMoves(vector<int>& balance) {
        int n = balance.size();
        int neg_index = -1;
        long long total_deficit = 0;
        
        // Find the index with negative balance and calculate total deficit
        for (int i = 0; i < n; ++i) {
            if (balance[i] < 0) {
                neg_index = i;
                total_deficit = -balance[i];
                break;
            }
        }
        
        // If there's no deficit, no moves are needed
        if (neg_index == -1) return 0;

        long long moves = 0;
        int current_index = (neg_index + 1) % n;
        
        while (total_deficit > 0 && current_index != neg_index) {
            if (balance[current_index] > 0) {
                long long transfer_amount = std::min(total_deficit, static_cast<long long>(balance[current_index]));
                total_deficit -= transfer_amount;
                balance[current_index] -= transfer_amount;
                moves += transfer_amount;
            }
            current_index = (current_index + 1) % n;
        }

        // Check if it's possible to balance
        if (total_deficit > 0) return -1;

        return moves;
    }
};
# @lc code=end