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
    int longestPalindrome(string s, string t) {
        int n = s.length();
        int m = t.length();
        int max_len = 0;

        auto isPalindrome = [](const string& str) {
            if (str.empty()) return false;
            int left = 0, right = str.length() - 1;
            while (left < right) {
                if (str[left++] != str[right--]) return false;
            }
            return true;
        };

        // Pre-extract all substrings of s including empty
        vector<string> subs_s;
        for (int i = 0; i <= n; ++i) {
            for (int len = 0; i + len <= n; ++len) {
                subs_s.push_back(s.substr(i, len));
            }
        }

        // Pre-extract all substrings of t including empty
        vector<string> subs_t;
        for (int i = 0; i <= m; ++i) {
            for (int len = 0; i + len <= m; ++len) {
                subs_t.push_back(t.substr(i, len));
            }
        }

        for (const string& sub1 : subs_s) {
            for (const string& sub2 : subs_t) {
                int current_len = sub1.length() + sub2.length();
                if (current_len > max_len) {
                    if (isPalindrome(sub1 + sub2)) {
                        max_len = current_len;
                    }
                }
            }
        }

        return max_len;
    }
};
# @lc code=end