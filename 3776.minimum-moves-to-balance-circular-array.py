#
# @lc app=leetcode id=3776 lang=python3
#
# [3776] Minimum Moves to Balance Circular Array
#

# @lc code=start
from typing import List

class Solution:
    def minMoves(self, balance: List[int]) -> int:
        n = len(balance)

        neg = -1
        for i, x in enumerate(balance):
            if x < 0:
                neg = i
                break

        # Already all non-negative
        if neg == -1:
            return 0

        # Total balance must be >= 0 to end with all non-negative
        if sum(balance) < 0:
            return -1

        need = -balance[neg]

        supplies = []  # (distance_to_neg, available_units)
        for i, x in enumerate(balance):
            if i == neg or x <= 0:
                continue
            diff = abs(i - neg)
            dist = min(diff, n - diff)
            supplies.append((dist, x))

        supplies.sort()

        moves = 0
        for dist, s in supplies:
            if need == 0:
                break
            take = s if s < need else need
            moves += take * dist
            need -= take

        return moves if need == 0 else -1
# @lc code=end
