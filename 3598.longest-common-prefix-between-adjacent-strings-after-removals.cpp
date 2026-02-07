#
# @lc app=leetcode id=3598 lang=cpp
#
# [3598] Longest Common Prefix Between Adjacent Strings After Removals
#
# @lc code=start
class Solution {
public:
    int longestCommonPrefixBetweenTwoStrings(const string& s1, const string& s2) {
        int minLength = min(s1.size(), s2.size());
        for (int i = 0; i < minLength; ++i) {
            if (s1[i] != s2[i]) {
                return i;
            }
        }
        return minLength;
    }
    vector<int> longestCommonPrefix(vector<string>& words) {
        vector<int> answer(words.size(), 0);
        int n = words.size();
        for (int i = 0; i < n; ++i) {
            int maxLength = 0;
            for (int j = 0; j < n - 1; ++j) {
                if (j == i || j + 1 == i) continue; // Skip the removed index and its next neighbor.
                int length = longestCommonPrefixBetweenTwoStrings(words[j], words[j + 1]);
                maxLength = max(maxLength, length);
            }
            answer[i] = maxLength;
        }
        return answer;
    }
};
# @lc code=end