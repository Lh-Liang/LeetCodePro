#
# @lc app=leetcode id=3598 lang=cpp
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
class Solution {
public:
    // Helper to compute the common prefix length
    int commonPrefix(const string& a, const string& b) {
        int len = min(a.size(), b.size());
        int i = 0;
        while (i < len && a[i] == b[i]) ++i;
        return i;
    }
    vector<int> longestCommonPrefix(vector<string>& words) {
        int n = words.size();
        if (n <= 1) return vector<int>(n, 0);
        vector<int> prefixLens(n-1);
        for (int i = 0; i < n-1; ++i) {
            prefixLens[i] = commonPrefix(words[i], words[i+1]);
        }
        // Precompute prefix maximums and suffix maximums for fast range max
        vector<int> prefixMax(n-1), suffixMax(n-1);
        prefixMax[0] = prefixLens[0];
        for (int i = 1; i < n-1; ++i) prefixMax[i] = max(prefixMax[i-1], prefixLens[i]);
        suffixMax[n-2] = prefixLens[n-2];
        for (int i = n-3; i >= 0; --i) suffixMax[i] = max(suffixMax[i+1], prefixLens[i]);
        vector<int> res(n);
        for (int i = 0; i < n; ++i) {
            int maxPrefix = 0;
            if (n == 2) {
                res[i] = 0;
                continue;
            }
            // Max among pairs before the removed index
            if (i > 1) maxPrefix = prefixMax[i-2];
            // Max among pairs after the removed index
            if (i < n-2) maxPrefix = max(maxPrefix, suffixMax[i+1]);
            // Max from the new adjacent pair formed by removal
            if (i > 0 && i < n-1) {
                int merged = commonPrefix(words[i-1], words[i+1]);
                maxPrefix = max(maxPrefix, merged);
            }
            res[i] = maxPrefix;
        }
        return res;
    }
};
# @lc code=end