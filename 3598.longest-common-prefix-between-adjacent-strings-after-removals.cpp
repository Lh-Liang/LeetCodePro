#
# @lc app=leetcode id=3598 lang=cpp
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#
# @lc code=start
class Solution {
public:
    vector<int> longestCommonPrefix(vector<string>& words) {
        int n = words.size();
        if (n <= 1) return vector<int>(n, 0);
        
        vector<int> result(n);
        vector<int> prefixLCP(n - 1), suffixLCP(n - 1);
        
        // Precompute LCP for adjacent pairs
        for (int i = 0; i < n - 1; ++i) {
            prefixLCP[i] = commonPrefixLength(words[i], words[i + 1]);
        }
        
        // Build prefix LCP sums
        for (int i = 1; i < n - 1; ++i) {
            prefixLCP[i] += prefixLCP[i - 1];
        }

        // Build suffix LCP sums
        suffixLCP[n - 2] = commonPrefixLength(words[n - 2], words[n - 1]);
        for (int i = n - 3; i >= 0; --i) {
            suffixLCP[i] = commonPrefixLength(words[i], words[i + 1]) + suffixLCP[i + 1];
        }
        
        // Calculate result for each removal
        for (int i = 0; i < n; ++i) {
            int maxLCP = 0;
            if (i > 0 && i < n - 1) {
                maxLCP = commonPrefixLength(words[i - 1], words[i + 1]);
            }
            if (i > 0) maxLCP = max(maxLCP, prefixLCP[i - 1]);
            if (i < n - 2) maxLCP = max(maxLCP, suffixLCP[i + 1]);
            result[i] = maxLCP;
        }

        return result;
    }
private:
    int commonPrefixLength(const string& s1, const string& s2) {
        int len = min(s1.length(), s2.length());
        int i = 0;
        while (i < len && s1[i] == s2[i]) { ++i; }
        return i;
    }
};
# @lc code=end