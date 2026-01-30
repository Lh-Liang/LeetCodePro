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
        if min(balance) >= 0:
            return 0
        neg_idx = -1
        for i, x in enumerate(balance):
            if x < 0:
                neg_idx = i
                break
        need = -balance[neg_idx]
        moves = 0
        l, r = (neg_idx - 1) % n, (neg_idx + 1) % n
        while need > 0:
            # Move from the side with more units
            if balance[l] >= balance[r]:
                take = min(need, balance[l])
                moves += take * min((neg_idx - l) % n, (l - neg_idx) % n)
                balance[l] -= take
                need -= take
                l = (l - 1) % n
            else:
                take = min(need, balance[r])
                moves += take * min((r - neg_idx) % n, (neg_idx - r) % n)
                balance[r] -= take
                need -= take
                r = (r + 1) % n
        return moves
# @lc code=end