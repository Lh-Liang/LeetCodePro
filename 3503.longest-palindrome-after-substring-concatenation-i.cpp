#
# @lc app=leetcode id=3503 lang=cpp
#
# [3503] Longest Palindrome After Substring Concatenation I
#

# @lc code=start
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

class Solution {
public:
    bool isPalindrome(const string& str) {
        if (str.empty()) return false;
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str[left] != str[right]) return false;
            left++;
            right--;
        }
        return true;
    }

    int longestPalindrome(string s, string t) {
        int n = s.length();
        int m = t.length();
        int maxLen = 0;

        vector<string> s_subs = {""};
        for (int i = 0; i < n; ++i) {
            for (int len = 1; i + len <= n; ++len) {
                s_subs.push_back(s.substr(i, len));
            }
        }

        vector<string> t_subs = {""};
        for (int i = 0; i < m; ++i) {
            for (int len = 1; i + len <= m; ++len) {
                t_subs.push_back(t.substr(i, len));
            }
        }

        for (const string& sub1 : s_subs) {
            for (const string& sub2 : t_subs) {
                string combined = sub1 + sub2;
                if (isPalindrome(combined)) {
                    maxLen = max(maxLen, (int)combined.length());
                }
            }
        }

        return maxLen;
    }
};
# @lc code=end