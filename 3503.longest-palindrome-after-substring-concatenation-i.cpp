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

        // Iterate over all possible substrings of s
        for (int i = 0; i <= n; ++i) {
            for (int len1 = 0; len1 <= n - i; ++len1) {
                // Iterate over all possible substrings of t
                for (int j = 0; j <= m; ++j) {
                    for (int len2 = 0; len2 <= m - j; ++len2) {
                        int total_len = len1 + len2;
                        if (total_len <= max_len) continue;

                        // Check if s[i...i+len1-1] + t[j...j+len2-1] is a palindrome
                        bool is_pal = true;
                        for (int k = 0; k < total_len / 2; ++k) {
                            char left, right;
                            
                            // Get character at index k
                            if (k < len1) {
                                left = s[i + k];
                            } else {
                                left = t[j + (k - len1)];
                            }

                            // Get character at index total_len - 1 - k
                            int opp = total_len - 1 - k;
                            if (opp < len1) {
                                right = s[i + opp];
                            } else {
                                right = t[j + (opp - len1)];
                            }

                            if (left != right) {
                                is_pal = false;
                                break;
                            }
                        }

                        if (is_pal) {
                            max_len = total_len;
                        }
                    }
                }
            }
        }

        return max_len;
    }
};
# @lc code=end