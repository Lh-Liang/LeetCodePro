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
        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + damage[i]
        total = 0
        for i in range(n):
            thresh = requirement[i] - hp + prefix[i + 1]
            j = bisect.bisect_left(prefix, thresh, 0, i + 1)
            total += i - j + 1
        return total
# @lc code=end