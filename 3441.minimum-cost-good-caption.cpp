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
        if(n < 3) return "";
        // dp[i] = {min_cost, lex smallest good caption for prefix of length i}
        vector<pair<int, string>> dp(n+1, {INT_MAX, ""});
        dp[0] = {0, ""};
        for(int i=3; i<=n; ++i) {
            for(int len=3; len<=i; ++len) {
                int start = i - len;
                for(char c='a'; c<='z'; ++c) {
                    int cost = 0;
                    for(int k=start; k<i; ++k) {
                        if(caption[k]!=c) cost++;
                    }
                    if(dp[start].first==INT_MAX) continue;
                    int total_cost = dp[start].first + cost;
                    string candidate = dp[start].second + string(len, c);
                    if(total_cost < dp[i].first || (total_cost==dp[i].first && candidate < dp[i].second)) {
                        dp[i] = {total_cost, candidate};
                    }
                }
            }
        }
        // Verification step: Ensure that the final result is a valid good caption
        if(dp[n].first==INT_MAX) return "";
        const string& res = dp[n].second;
        int i = 0;
        while(i < n) {
            int j = i;
            while(j < n && res[j] == res[i]) ++j;
            if(j - i < 3) return "";
            i = j;
        }
        return res;
    }
};
# @lc code=end