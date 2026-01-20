#
# @lc app=leetcode id=3598 lang=cpp
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> longestCommonPrefix(vector<string>& words) {
        int n = words.size();
        if (n == 0) return {};
        if (n == 1) return {0};

        auto getLCP = [](const string& a, const string& b) {
            int len = 0;
            int minLen = min((int)a.length(), (int)b.length());
            while (len < minLen && a[len] == b[len]) {
                len++;
            }
            return len;
        };

        // L[i] is LCP of words[i] and words[i+1]
        vector<int> L(n - 1);
        for (int i = 0; i < n - 1; ++i) {
            L[i] = getLCP(words[i], words[i + 1]);
        }

        // pref[i] is max(L[0]...L[i-1])
        vector<int> pref(n, 0);
        for (int i = 1; i < n; ++i) {
            pref[i] = max(pref[i - 1], L[i - 1]);
        }

        // suff[i] is max(L[i]...L[n-2])
        vector<int> suff(n, 0);
        for (int i = n - 2; i >= 0; --i) {
            suff[i] = max(suff[i + 1], L[i]);
        }

        vector<int> ans(n);
        for (int i = 0; i < n; ++i) {
            // Original pairs excluding those involving words[i]
            int left_max = (i >= 2) ? pref[i - 1] : 0;
            int right_max = (i <= n - 3) ? suff[i + 1] : 0;
            
            // New pair formed by removing words[i]
            int mid_lcp = 0;
            if (i >= 1 && i <= n - 2) {
                mid_lcp = getLCP(words[i - 1], words[i + 1]);
            }
            
            ans[i] = max({left_max, right_max, mid_lcp});
        }

        return ans;
    }
};
# @lc code=end