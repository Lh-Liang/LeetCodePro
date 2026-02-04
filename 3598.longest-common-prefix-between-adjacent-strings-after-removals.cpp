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
        vector<int> result(n, 0);
        
        // Helper function to calculate longest common prefix of two strings
        auto lcp = [](const string& a, const string& b) {
            int minLength = min(a.size(), b.size());
            for (int i = 0; i < minLength; ++i) {
                if (a[i] != b[i]) return i;
            }
            return minLength;
        };
        
        // Iterate over each word removed scenario
        for (int i = 0; i < n; ++i) {
            int maxLCP = 0;
            for (int j = 0; j < n - 1; ++j) {
                if (j == i || j + 1 == i) continue; // Skip over removed index and its next pair 
                maxLCP = max(maxLCP, lcp(words[j], words[j + 1])); 
            } 
            result[i] = maxLCP; 
        } 
        return result; 
    } 
}; 
# @lc code=end