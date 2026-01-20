#
# @lc app=leetcode id=3771 lang=python3
#
# [3771] Total Score of Dungeon Runs
#

# @lc code=start
from bisect import bisect_left
from typing import List

class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        # prefix_damage[k] stores sum of damage[0]...damage[k-1]
        # prefix_damage[0] = 0
        prefix_damage = [0] * (n + 1)
        for i in range(n):
            prefix_damage[i+1] = prefix_damage[i] + damage[i]
        
        total_points = 0
        
        # Iterate through each room 'i' considering it as the room where we potentially score a point.
        # We need to find how many starting rooms 'j' (where 1 <= j <= i+1) satisfy the condition.
        # In 0-indexed terms, let current room be 'i' (0 to n-1).
        # Starting room 'j' corresponds to index 'start_idx' (0 to i).
        # Damage taken from start_idx to i is: prefix_damage[i+1] - prefix_damage[start_idx]
        # Condition: hp - (prefix_damage[i+1] - prefix_damage[start_idx]) >= requirement[i]
        # Rearranging: prefix_damage[start_idx] >= prefix_damage[i+1] + requirement[i] - hp
        
        for i in range(n):
            target = prefix_damage[i+1] + requirement[i] - hp
            
            # We need to count valid 'start_idx' in range [0, i] such that 
            # prefix_damage[start_idx] >= target.
            # Since prefix_damage is sorted (damages are positive), we can use binary search.
            
            # Find the first index 'k' in prefix_damage such that prefix_damage[k] >= target.
            # We are only interested in indices up to 'i'.
            # Actually, the search space for start_idx is 0 to i.
            # However, bisect_left on the whole array or a slice is fine, but we only care if the found index <= i.
            
            # Optimization: since we need start_idx in [0, i], we can search in that range specifically
            # or just search globally and cap the result.
            # Let's search in the full prefix_damage array but interpret result.
            
            idx = bisect_left(prefix_damage, target, 0, i + 1)
            
            # All indices from 'idx' to 'i' satisfy the condition because prefix_damage is increasing.
            # The number of such indices is (i - idx + 1).
            if idx <= i:
                total_points += (i - idx + 1)
                
        return total_points

# @lc code=end