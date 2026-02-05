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
        vector<long long> prefix(n + 1, 0);
        for (int i = 0; i < n; ++i) {
            prefix[i + 1] = prefix[i] + damage[i];
        }
        vector<long long> diff(n + 2, 0);
        for (int i = 0; i < n; ++i) {
            // We want to find the earliest start index j such that:
            // hp - (prefix[i + 1] - prefix[j]) >= requirement[i]
            // <=> prefix[j] <= hp - requirement[i] + prefix[i + 1]
            long long target = hp - requirement[i] + prefix[i + 1];
            // Binary search for leftmost j in [0, i + 1) such that prefix[j] <= target
            int l = 0, r = i + 1;
            int res = i + 1;
            while (l < r) {
                int m = (l + r) / 2;
                if (prefix[m] <= target) {
                    res = m;
                    r = m;
                } else {
                    l = m + 1;
                }
            }
            if (res <= i) {
                diff[res] += 1;
                diff[i + 1] -= 1;
            }
        }
        long long ans = 0, cur = 0;
        for (int i = 0; i < n; ++i) {
            cur += diff[i];
            ans += cur;
        }
        return ans;
    }
};
# @lc code=end