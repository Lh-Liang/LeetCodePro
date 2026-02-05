#
# @lc app=leetcode id=3445 lang=cpp
#
# [3445] Maximum Difference Between Even and Odd Frequency II
#

# @lc code=start
class Solution {
public:
    int maxDifference(string s, int k) {
        int n = s.length();
        // prefix[d][i]: count of digit d in s[0..i-1]
        int prefix[5][30005] = {};
        for (int d = 0; d < 5; ++d) prefix[d][0] = 0;
        for (int i = 0; i < n; ++i) {
            for (int d = 0; d < 5; ++d) {
                prefix[d][i+1] = prefix[d][i] + (s[i] == ('0'+d) ? 1 : 0);
            }
        }
        int ans = -1;
        for (int l = 0; l <= n - k; ++l) {
            for (int r = l + k; r <= n; ++r) {
                // freq[d]: frequency of digit d in s[l..r-1]
                int freq[5] = {};
                for (int d = 0; d < 5; ++d) {
                    freq[d] = prefix[d][r] - prefix[d][l];
                }
                for (int a = 0; a < 5; ++a) {
                    if (freq[a] % 2 == 1) {
                        for (int b = 0; b < 5; ++b) {
                            if (a != b && freq[b] > 0 && freq[b] % 2 == 0) {
                                ans = max(ans, freq[a] - freq[b]);
                            }
                        }
                    }
                }
            }
        }
        return ans;
    }
};
# @lc code=end