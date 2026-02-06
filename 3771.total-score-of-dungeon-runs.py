#
# @lc app=leetcode id=3771 lang=python3
#
# [3771] Total Score of Dungeon Runs
#

# @lc code=start
class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        n = len(damage)
        total_score = 0
        
        # Iterate over each room as a starting point
        for start in range(n):
            current_hp = hp
            score = 0
            
            # Simulate entering each subsequent room from 'start'
            for i in range(start, n):
                current_hp -= damage[i]
                if current_hp >= requirement[i]:
                    score += 1
            
            # Add scores from this starting point to total score
            total_score += score
        
        return total_score
# @lc code=end