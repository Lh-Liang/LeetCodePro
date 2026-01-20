#
# @lc app=leetcode id=3598 lang=cpp
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#

# @lc code=start
class Solution {
public:
    // Helper to compute LCP of two strings
    int computeLCP(const string& a, const string& b) {
        int n = min(a.length(), b.length());
        int i = 0;
        while (i < n && a[i] == b[i]) {
            i++;
        }
        return i;
    }

    vector<int> longestCommonPrefix(vector<string>& words) {
        int n = words.size();
        if (n == 1) return {0};

        // adjLCP[i] stores LCP(words[i], words[i+1])
        // Size is n-1
        vector<int> adjLCP(n - 1, 0);
        for (int i = 0; i < n - 1; ++i) {
            adjLCP[i] = computeLCP(words[i], words[i+1]);
        }

        // Precompute prefix maximums for adjLCP
        vector<int> prefixMax(n - 1, 0);
        if (n > 1) {
            prefixMax[0] = adjLCP[0];
            for (int i = 1; i < n - 1; ++i) {
                prefixMax[i] = max(prefixMax[i - 1], adjLCP[i]);
            }
        }

        // Precompute suffix maximums for adjLCP
        vector<int> suffixMax(n - 1, 0);
        if (n > 1) {
            suffixMax[n - 2] = adjLCP[n - 2];
            for (int i = n - 3; i >= 0; --i) {
                suffixMax[i] = max(suffixMax[i + 1], adjLCP[i]);
            }
        }

        vector<int> answer(n);
        for (int i = 0; i < n; ++i) {
            int maxVal = 0;

            // 1. Max from left side (unaffected pairs before i-1)
            // We need max of adjLCP[0...i-2]
            if (i >= 2) {
                maxVal = max(maxVal, prefixMax[i - 2]);
            }

            // 2. Max from right side (unaffected pairs after i)
            // We need max of adjLCP[i+1...n-2]
            if (i < n - 2) {
                maxVal = max(maxVal, suffixMax[i + 1]);
            }

            // 3. The new pair formed by removing words[i]: (words[i-1], words[i+1])
            if (i > 0 && i < n - 1) {
                maxVal = max(maxVal, computeLCP(words[i - 1], words[i + 1]));
            }

            answer[i] = maxVal;
        }

        return answer;
    }
};
# @lc code=end