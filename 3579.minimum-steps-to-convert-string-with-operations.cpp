//
// @lc app=leetcode id=3579 lang=cpp
//
// [3579] Minimum Steps to Convert String with Operations
//

// @lc code=start
class Solution {
public:
    int minOperations(string word1, string word2) {
        int n = word1.length();
        
        auto segmentCost = [&](int l, int r, bool reverse_s) -> int {
            int count[26][26] = {};
            int diff = 0;
            
            for (int i = l; i <= r; i++) {
                char c1 = reverse_s ? word1[l + r - i] : word1[i];
                char c2 = word2[i];
                if (c1 != c2) {
                    diff++;
                    count[c1 - 'a'][c2 - 'a']++;
                }
            }
            
            int savings = 0;
            for (int a = 0; a < 26; a++) {
                for (int b = a + 1; b < 26; b++) {
                    savings += min(count[a][b], count[b][a]);
                }
            }
            
            return (reverse_s ? 1 : 0) + diff - savings;
        };
        
        vector<int> dp(n + 1, INT_MAX);
        dp[0] = 0;
        
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < i; j++) {
                int cost = min(segmentCost(j, i - 1, false), segmentCost(j, i - 1, true));
                dp[i] = min(dp[i], dp[j] + cost);
            }
        }
        
        return dp[n];
    }
};
// @lc code=end