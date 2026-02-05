#
# @lc app=leetcode id=3598 lang=cpp
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#
# @lc code=start
class Solution {
public:
    // Helper to compute length of longest common prefix of a and b
    int lcp(const string& a, const string& b) {
        int n = min(a.size(), b.size());
        int i = 0;
        while (i < n && a[i] == b[i]) ++i;
        return i;
    }
    vector<int> longestCommonPrefix(vector<string>& words) {
        int n = words.size();
        if (n <= 1) return vector<int>(n, 0);
        vector<int> pre(n-1);
        // Step 1: Precompute prefix lengths for all adjacent pairs
        for (int i = 0; i < n-1; ++i) {
            pre[i] = lcp(words[i], words[i+1]);
        }
        // Step 2: For each removal, calculate the result
        vector<int> ans(n, 0);
        for (int i = 0; i < n; ++i) {
            int max_lcp = 0;
            // For removal at i, affected pairs: (i-1,i) and (i,i+1), new pair: (i-1,i+1)
            if (n == 2) {
                // Only one pair exists, after removal no pair remains
                ans[i] = 0;
                continue;
            }
            // Compute max among unaffected pairs
            // Pairs before (i-1,i): pre[0..i-2]
            for (int j = 0; j < i-1; ++j) max_lcp = max(max_lcp, pre[j]);
            // Pairs after (i,i+1): pre[i+1..n-2]
            for (int j = i+1; j < n-1; ++j) max_lcp = max(max_lcp, pre[j]);
            // Now, handle the new pair (i-1,i+1) if both are in bounds
            if (i > 0 && i < n-1) {
                int new_lcp = lcp(words[i-1], words[i+1]);
                max_lcp = max(max_lcp, new_lcp);
            }
            ans[i] = max_lcp;
        }
        return ans;
    }
};
# @lc code=end