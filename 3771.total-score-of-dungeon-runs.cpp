#
# @lc app=leetcode id=3771 lang=cpp
#
# [3771] Total Score of Dungeon Runs
#
# @lc code=start
class Solution {
public:
    long long totalScore(int hp, vector<int>& damage, vector<int>& requirement) {
        int n = damage.size();
        long long total_score = 0;
        for (int j = 0; j < n; ++j) {
            int current_hp = hp;
            int score_j = 0;
            for (int i = j; i < n; ++i) {
                current_hp -= damage[i];
                if (current_hp >= requirement[i]) {
                    ++score_j;
                }
            }
            total_score += score_j;
        }
        return total_score;
    }
};
# @lc code=end