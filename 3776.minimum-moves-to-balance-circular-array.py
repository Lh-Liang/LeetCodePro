#
# @lc app=leetcode id=3776 lang=python3
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0:
            return -1

        n = len(balance)
        moves = 0
        neg_index = next((i for i in range(n) if balance[i] < 0), None)
        if neg_index is None:
            return 0  # No negative balance means no moves needed.
        
        while balance[neg_index] < 0:
            for i in range(n):
                if balance[i] > 0:
                    transfer_amount = min(-balance[neg_index], balance[i])
                    balance[i] -= transfer_amount
                    balance[neg_index] += transfer_amount
                    moves += transfer_amount
                if balance[neg_index] >= 0:
                    break
            neg_index = (neg_index + 1) % n # Circular array consideration.
        
        return moves # @lc code=end