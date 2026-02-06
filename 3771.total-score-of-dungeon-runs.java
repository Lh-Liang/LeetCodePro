#
# @lc app=leetcode id=3771 lang=java
#
# [3771] Total Score of Dungeon Runs
#

# @lc code=start
class Solution {
    public long totalScore(int hp, int[] damage, int[] requirement) {
        int n = damage.length;
        // prefix sum of damage
        long[] prefix = new long[n + 1];
        for (int i = 0; i < n; i++) {
            prefix[i + 1] = prefix[i] + damage[i];
        }
        long total = 0;
        // For each start index
        for (int start = 0; start < n; start++) {
            long curHP = hp;
            int score = 0;
            for (int i = start; i < n; i++) {
                curHP -= damage[i];
                if (curHP >= requirement[i]) {
                    score++;
                }
            }
            total += score;
        }
        return total;
    }
}
# @lc code=end