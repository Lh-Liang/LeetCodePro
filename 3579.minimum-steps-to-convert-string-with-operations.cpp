#
# @lc app=leetcode id=3579 lang=cpp
#
# [3579] Minimum Steps to Convert String with Operations
#

# @lc code=start
class Solution {
public:
    int minOperations(string word1, string word2) {
        int n = word1.size();
        vector<vector<int>> dp(n+1, vector<int>(n+1, 1e9));
        for (int i = 0; i <= n; ++i) dp[i][i] = 0;
        for (int len = 1; len <= n; ++len) {
            for (int i = 0; i + len <= n; ++i) {
                int j = i + len;
                string s1 = word1.substr(i, len);
                string s2 = word2.substr(i, len);
                int cost = 1e9;
                if (s1 == s2) cost = 0;
                else {
                    // Reverse
                    string rev = s1; reverse(rev.begin(), rev.end());
                    if (rev == s2) cost = 1;
                    // Swap
                    for (int x = 0; x < len; ++x) {
                        for (int y = x+1; y < len; ++y) {
                            string t = s1;
                            swap(t[x], t[y]);
                            if (t == s2) cost = min(cost, 1);
                        }
                    }
                    // Replace
                    int rep = 0;
                    for (int k = 0; k < len; ++k) rep += (s1[k] != s2[k]);
                    cost = min(cost, rep);
                }
                dp[i][j] = cost;
                // Try split
                for (int k = i+1; k < j; ++k) {
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j]);
                }
            }
        }
        return dp[0][n];
    }
};
# @lc code=end