#
# @lc app=leetcode id=3771 lang=java
#
# [3771] Total Score of Dungeon Runs
#
# @lc code=start
class Solution {
    public long totalScore(int hp, int[] damage, int[] requirement) {
        long total_score = 0;
        int n = damage.length;
        for (int i = 0; i < n; i++) {
            int current_hp = hp;
            int score = 0;
            for (int j = i; j < n; j++) {
                current_hp -= damage[j];
                if (current_hp >= requirement[j]) {
                    score++;
                }
            }
            total_score += score;
        }
        return total_score;
    }
}
# @lc code=end