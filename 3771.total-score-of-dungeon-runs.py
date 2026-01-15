#
# @lc app=leetcode id=3771 lang=python3
#
# [3771] Total Score of Dungeon Runs
#

import bisect
from typing import List

# @lc code=start
class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        # Prefix sums of damages
        pref = [0] * (n + 1)
        for i in range(1, n + 1):
            pref[i] = pref[i - 1] + damage[i - 1]
        
        ans = 0
        # For each room i (1-indexed)
        for i in range(1, n + 1):
            # Threshold value for starting indices
            threshold = pref[i] + requirement[i - 1] - hp
            # First index where pref[idx] >= threshold
            pos = bisect.bisect_left(pref, threshold)
            # Count of valid starting positions j <= i
            cnt = max(0, i - pos)
            ans += cnt
        return ans
# @lc code=end