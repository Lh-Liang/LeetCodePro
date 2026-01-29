#
# @lc app=leetcode id=3771 lang=python3
#
# [3771] Total Score of Dungeon Runs
#

# @lc code=start
from typing import List
from bisect import bisect_left

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        # Calculate prefix sums of damage: P[i] = damage[0] + ... + damage[i-1]
        P = [0] * (n + 1)
        for i in range(n):
            P[i + 1] = P[i] + damage[i]
        
        total_score = 0
        # Iterate through each room i to find its contribution to the total score.
        # A starting room j (1 <= j <= i) contributes a point if:
        # hp - (P[i] - P[j-1]) >= requirement[i-1]
        # Rearranging: P[j-1] >= requirement[i-1] + P[i] - hp
        for i in range(1, n + 1):
            target = requirement[i-1] + P[i] - hp
            
            # We need to count indices k in [0, i-1] such that P[k] >= target.
            # Since P is strictly increasing, we find the first index 'idx' where P[idx] >= target.
            # Every index from 'idx' up to 'i-1' will satisfy the condition.
            idx = bisect_left(P, target, lo=0, hi=i)
            
            # Number of valid starting rooms j is (i - idx)
            total_score += (i - idx)
            
        return total_score
# @lc code=end