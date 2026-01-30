#
# @lc app=leetcode id=3771 lang=python3
#
# [3771] Total Score of Dungeon Runs
#

# @lc code=start
from typing import List
import bisect

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        prefix_damage = [0] * (n + 1)
        for i in range(n):
            prefix_damage[i+1] = prefix_damage[i] + damage[i]

        total = 0
        for i in range(n):
            threshold = hp - requirement[i] + prefix_damage[i+1]
            # Find largest pos such that prefix_damage[pos] <= threshold
            # Valid j are from 1 to pos+1 (as j-1 = pos) and j <= i+1
            pos = bisect.bisect_right(prefix_damage, threshold, 0, i+1) - 1
            valid_starts = max(0, pos + 1)
            total += valid_starts
        return total
# @lc code=end