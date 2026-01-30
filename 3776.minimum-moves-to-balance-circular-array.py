#
# @lc app=leetcode id=3776 lang=python3
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        total_balance = sum(balance)
        if total_balance < 0:
            return -1  # Impossible to make all balances non-negative
        n = len(balance)
        index = balance.index(min(balance))  # Find the index with negative balance
        moves = 0
        for i in range(index + 1, index + n):  # Traverse circularly both sides
            pos = i % n
            if balance[pos] > 0:
                move = min(balance[pos], -balance[index])
                moves += move
                balance[pos] -= move
                balance[index] += move
            if balance[index] >= 0:
                break
        return moves if all(b >= 0 for b in balance) else -1
# @lc code=end