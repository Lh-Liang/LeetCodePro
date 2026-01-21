#
# @lc app=leetcode id=3458 lang=cpp
#
# [3458] Select K Disjoint Special Substrings
#

# @lc code=start
class Solution {
public:
    bool maxSubstringLength(string s, int k) {
        int n = s.size();
        vector<int> minpos(26, n);
        vector<int> maxpos(26, -1);
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            minpos[c] = min(minpos[c], i);
            maxpos[c] = max(maxpos[c], i);
        }
        vector<int> Left(n), Right(n);
        for (int i = 0; i < n; ++i) {
            int c = s[i] - 'a';
            Left[i] = minpos[c];
            Right[i] = maxpos[c];
        }
        vector<int> dp(n + 1, 0);
        for (int i = n - 1; i >= 0; --i) {
            int fb = i;
            while (fb < n && Left[fb] >= i) ++fb;
            int endd = fb - 1;
            int best = 0;
            if (endd >= i) {
                int cur_maxr = -1;
                for (int j = i; j <= endd; ++j) {
                    cur_maxr = max(cur_maxr, Right[j]);
                    if (cur_maxr <= j && !(i == 0 && j == n - 1)) {
                        best = max(best, 1 + dp[j + 1]);
                    }
                }
            }
            dp[i] = max(dp[i + 1], best);
        }
        return dp[0] >= k;
    }
};
# @lc code=end