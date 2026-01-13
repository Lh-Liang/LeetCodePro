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
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + damage[i - 1]

        ans = 0
        for i in range(1, n + 1):
            threshold = pref[i] + requirement[i - 1] - hp
            # count k in [0..i-1] with pref[k] >= threshold
            idx = bisect.bisect_left(pref, threshold, 0, i)
            ans += i - idx
        return ans
# @lc code=end
