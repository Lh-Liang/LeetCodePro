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
        long long total = 0;
        
        // Iterate over all starting positions from 1 to n
        for (int start = 0; start < n; ++start) {
            int current_hp = hp;
            long long score = 0;
            // Traverse from current start position to end
            for (int i = start; i < n; ++i) {
                current_hp -= damage[i];
                if (current_hp >= requirement[i]) {
                    ++score;
                } else if (current_hp <= 0) { // No point in going further if HP is non-positive
                    break;
                }
            }
            total += score; // Add score from this starting point to total score. 
        }
        return total; 
    } 
}; 
# @lc code=end