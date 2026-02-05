#
# @lc app=leetcode id=3734 lang=cpp
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.size();
        vector<int> cnt(26, 0);
        for (char c : s) cnt[c - 'a']++;
        int odd = 0, odd_char = -1;
        for (int i = 0; i < 26; ++i) {
            if (cnt[i] % 2) {
                odd++;
                odd_char = i;
            }
        }
        if (odd > 1) return "";
        string half = "";
        for (int i = 0; i < 26; ++i) half += string(cnt[i]/2, 'a' + i);
        string middle = odd_char != -1 ? string(1, 'a' + odd_char) : "";
        string smallest = half + middle + string(half.rbegin(), half.rend());
        if (smallest > target) return smallest;
        sort(half.begin(), half.end());
        do {
            string candidate = half + middle + string(half.rbegin(), half.rend());
            if (candidate > target) return candidate;
        } while (next_permutation(half.begin(), half.end()));
        return "";
    }
};
# @lc code=end