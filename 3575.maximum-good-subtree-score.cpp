//
// @lc app=leetcode id=3575 lang=cpp
//
// [3575] Maximum Good Subtree Score
//

// @lc code=start
class Solution {
public:
    int goodSubtreeSum(vector<int>& vals, vector<int>& par) {
        const int MOD = 1e9 + 7;
        int n = vals.size();
        
        vector<vector<int>> children(n);
        for (int i = 1; i < n; i++) {
            children[par[i]].push_back(i);
        }
        
        auto getDigitMask = [](int val) -> int {
            int mask = 0;
            while (val > 0) {
                int d = val % 10;
                if (mask & (1 << d)) return -1;
                mask |= (1 << d);
                val /= 10;
            }
            return mask;
        };
        
        vector<int> masks(n);
        for (int i = 0; i < n; i++) {
            masks[i] = getDigitMask(vals[i]);
        }
        
        long long totalSum = 0;
        const long long NEG_INF = -1e18;
        
        function<vector<long long>(int)> dfs = [&](int u) -> vector<long long> {
            vector<long long> dp(1024, NEG_INF);
            dp[0] = 0;
            
            for (int c : children[u]) {
                vector<long long> child_dp = dfs(c);
                vector<long long> new_dp(1024, NEG_INF);
                
                for (int m = 0; m < 1024; m++) {
                    for (int s = m; ; s = (s - 1) & m) {
                        if (dp[s] > NEG_INF && child_dp[m ^ s] > NEG_INF) {
                            new_dp[m] = max(new_dp[m], dp[s] + child_dp[m ^ s]);
                        }
                        if (s == 0) break;
                    }
                }
                dp = move(new_dp);
            }
            
            if (masks[u] != -1) {
                vector<long long> new_dp = dp;
                for (int m = 0; m < 1024; m++) {
                    if (dp[m] > NEG_INF && (m & masks[u]) == 0) {
                        new_dp[m | masks[u]] = max(new_dp[m | masks[u]], dp[m] + vals[u]);
                    }
                }
                dp = move(new_dp);
            }
            
            long long maxScore = 0;
            for (int m = 0; m < 1024; m++) {
                if (dp[m] > maxScore) {
                    maxScore = dp[m];
                }
            }
            totalSum = (totalSum + maxScore) % MOD;
            
            return dp;
        };
        
        dfs(0);
        return totalSum;
    }
};
// @lc code=end