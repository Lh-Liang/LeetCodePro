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
        vector<int> result(n);
        auto lcp = [](const string& a, const string& b) {
            int len = min(a.size(), b.size());
            for (int i = 0; i < len; ++i) {
                if (a[i] != b[i]) return i;
            }
            return len;
        };
        for (int i = 0; i < n; ++i) {
            vector<string> modifiedWords;
            for (int j = 0; j < n; ++j) {
                if (j != i) modifiedWords.push_back(words[j]);
            }
            int maxLCP = 0;
            for (int j = 0; j < modifiedWords.size() - 1; ++j) {
                maxLCP = max(maxLCP, lcp(modifiedWords[j], modifiedWords[j + 1]));
            }
            result[i] = maxLCP;
        }
        return result;
    }
};
# @lc code=end