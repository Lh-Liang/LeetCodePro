# @lc app=leetcode id=3575 lang=cpp
# [3575] Maximum Good Subtree Score

# @lc code=start
class Solution {
public:
    int goodSubtreeSum(vector<int>& vals, vector<int>& par) {
        const int MOD = 1e9 + 7;
        int n = vals.size();
        vector<vector<int>> tree(n);
        for (int i = 1; i < n; ++i) {
            tree[par[i]].push_back(i);
        }

        vector<int> maxScore(n, 0);
        function<void(int, set<int>&)> dfs = [&](int u, set<int>& parentDigits) {
            set<int> currentDigits = parentDigits;
            int val = vals[u];
            while (val > 0) {
                int digit = val % 10;
                if (currentDigits.count(digit)) {
                    return; // If digit repeats, exit as this can't be a good subset
                }
                currentDigits.insert(digit);
                val /= 10;
            }
            int totalScore = vals[u];
            for (int v : tree[u]) {
                dfs(v, currentDigits);
                totalScore += maxScore[v];
            }
            maxScore[u] = totalScore % MOD;
        };

        set<int> initialDigits;
        dfs(0, initialDigits);
        int result = accumulate(maxScore.begin(), maxScore.end(), 0LL) % MOD;
        return result;
    }
};
# @lc code=end