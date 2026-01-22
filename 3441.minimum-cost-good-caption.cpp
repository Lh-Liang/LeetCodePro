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
        if (n < 3) return "";
        
        const int INF = 1e9;
        
        // Forward DP: dp[i][k][c] - k=0,1,2 for 1,2,>=3 chars in group with char c
        vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(3, vector<int>(26, INF)));
        vector<int> dpB(n + 1, INF);
        dpB[0] = 0;
        
        for (int i = 0; i < n; i++) {
            int ch = caption[i] - 'a';
            int minValid = *min_element(dp[i][2].begin(), dp[i][2].end());
            
            for (int c = 0; c < 26; c++) {
                int cost = abs(ch - c);
                dp[i + 1][0][c] = min({dp[i + 1][0][c], dpB[i] + cost, minValid + cost});
                dp[i + 1][1][c] = min(dp[i + 1][1][c], dp[i][0][c] + cost);
                dp[i + 1][2][c] = min({dp[i + 1][2][c], dp[i][1][c] + cost, dp[i][2][c] + cost});
            }
            dpB[i + 1] = *min_element(dp[i + 1][2].begin(), dp[i + 1][2].end());
        }
        
        int minCost = dpB[n];
        if (minCost >= INF) return "";
        
        // Backward DP for reconstruction
        vector<vector<vector<int>>> dp2(n + 1, vector<vector<int>>(3, vector<int>(26, INF)));
        for (int c = 0; c < 26; c++) dp2[n][2][c] = 0;
        
        for (int i = n - 1; i >= 0; i--) {
            int ch = caption[i] - 'a';
            int minStart = *min_element(dp2[i + 1][0].begin(), dp2[i + 1][0].end());
            
            for (int c = 0; c < 26; c++) {
                int cost = abs(ch - c);
                dp2[i][0][c] = min(dp2[i][0][c], dp2[i + 1][1][c] + cost);
                dp2[i][1][c] = min(dp2[i][1][c], dp2[i + 1][2][c] + cost);
                dp2[i][2][c] = min({dp2[i][2][c], dp2[i + 1][2][c] + cost, minStart + cost});
            }
        }
        
        // Greedy reconstruction
        string result;
        int state = -1, curChar = -1;
        
        for (int i = 0; i < n; i++) {
            int ch = caption[i] - 'a';
            
            if (state == -1) {
                int baseVal = dpB[i];
                for (int c = 0; c < 26; c++) {
                    int cost = abs(ch - c);
                    if (baseVal + cost + dp2[i + 1][0][c] == minCost) {
                        result += (char)('a' + c);
                        state = 0; curChar = c;
                        break;
                    }
                }
            } else if (state == 0) {
                result += (char)('a' + curChar);
                state = 1;
            } else if (state == 1) {
                result += (char)('a' + curChar);
                state = 2;
            } else {
                int cost = abs(ch - curChar);
                bool extended = false;
                if (dp[i][2][curChar] + cost + dp2[i + 1][2][curChar] == minCost) {
                    for (int c = 0; c < curChar; c++) {
                        int newCost = abs(ch - c);
                        if (dp[i][2][curChar] + newCost + dp2[i + 1][0][c] == minCost) {
                            result += (char)('a' + c);
                            state = 0; curChar = c;
                            extended = true;
                            break;
                        }
                    }
                    if (!extended) {
                        result += (char)('a' + curChar);
                        extended = true;
                    }
                } else {
                    for (int c = 0; c < 26; c++) {
                        int newCost = abs(ch - c);
                        if (dp[i][2][curChar] + newCost + dp2[i + 1][0][c] == minCost) {
                            result += (char)('a' + c);
                            state = 0; curChar = c;
                            extended = true;
                            break;
                        }
                    }
                }
            }
        }
        
        return result;
    }
};
# @lc code=end