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
        vector<int> scores(n, 0);
        long long total = 0;
        
        // Compute scores backwards
        for (int start = n - 1; start >= 0; --start) {
            int current_hp = hp;
            int score = 0;
            for (int i = start; i < n; ++i) {
                current_hp -= damage[i];
                if (current_hp >= requirement[i]) {
                    ++score;
                }
            }
            scores[start] = score;
            total += score;
        }
        return total;
    }
}; 
# @lc code=end