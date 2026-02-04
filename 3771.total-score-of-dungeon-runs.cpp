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
        // Precompute prefix sums of damage
        vector<long long> prefix_damage(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix_damage[i + 1] = prefix_damage[i] + damage[i];
        }
        long long ans = 0;
        // For each room i, count the number of starting positions j <= i such that
        // hp - (prefix_damage[i+1] - prefix_damage[j]) >= requirement[i]
        // Rearranged: prefix_damage[j] >= requirement[i] + prefix_damage[i+1] - hp
        for (int i = 0; i < n; ++i) {
            long long threshold = requirement[i] + prefix_damage[i+1] - hp;
            auto it = lower_bound(prefix_damage.begin(), prefix_damage.begin() + i + 1, threshold);
            ans += (prefix_damage.begin() + i + 1) - it;
        }
        return ans;
    }
};
# @lc code=end