#
# @lc app=leetcode id=3441 lang=cpp
#
# [3441] Minimum Cost Good Caption
#

# @lc code=start
class Solution {
public:
    string minCostGoodCaption(string caption) {
        int n = caption.size();
        const int INF = 1e9;
        // dp[i] = {min_ops, answer string}
        vector<pair<int, string>> dp(n+1, {INF, ""});
        dp[0] = {0, ""}; // empty prefix
        for (int i = 0; i < n; ++i) {
            for (int len = 3; len <= i+1; ++len) {
                int j = i - len + 1;
                if (j < 0) break;
                for (char ch = 'a'; ch <= 'z'; ++ch) {
                    int cost = 0;
                    for (int k = j; k <= i; ++k) {
                        if (caption[k] != ch) cost++;
                    }
                    auto prev = dp[j];
                    if (prev.first != INF) {
                        string cand = prev.second + string(len, ch);
                        if (cost + prev.first < dp[i+1].first) {
                            dp[i+1] = {cost + prev.first, cand};
                        } else if (cost + prev.first == dp[i+1].first && cand < dp[i+1].second) {
                            dp[i+1].second = cand;
                        }
                    }
                }
            }
        }
        return dp[n].first == INF ? "" : dp[n].second;
    }
};
# @lc code=end