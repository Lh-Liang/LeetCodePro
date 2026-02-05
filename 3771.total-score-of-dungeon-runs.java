#
# @lc app=leetcode id=3771 lang=java
#
# [3771] Total Score of Dungeon Runs
#

# @lc code=start
class Solution {
    public long totalScore(int hp, int[] damage, int[] requirement) {
        int n = damage.length;
        long totalScore = 0;
        
        // Iterate over each starting room
        for (int start = 0; start < n; start++) {
            int currentHp = hp;
            int currentScore = 0;
            
            // Calculate score starting from room 'start'
            for (int i = start; i < n; i++) {
                currentHp -= damage[i];
                if (currentHp >= requirement[i]) {
                    currentScore++;
                }
            }
            totalScore += currentScore;
        }
        
        return totalScore;
    }
}
# @lc code=end