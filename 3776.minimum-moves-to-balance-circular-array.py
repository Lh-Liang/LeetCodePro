#
# @lc app=leetcode id=3776 lang=python3
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)
        total = sum(balance)
        if total < 0:
            return -1
        neg = -1
        d = 0
        for i in range(n):
            if balance[i] < 0:
                neg = i
                d = -balance[i]
                break
        if neg == -1:
            return 0
        moves = 0
        need = d
        for r in range(1, n // 2 + 1):
            p1 = (neg + r) % n
            p2 = (neg - r) % n
            cap = balance[p1]
            if p1 != p2:
                cap += balance[p2]
            take = min(need, cap)
            moves += take * r
            need -= take
            if need <= 0:
                break
        return moves
# @lc code=end