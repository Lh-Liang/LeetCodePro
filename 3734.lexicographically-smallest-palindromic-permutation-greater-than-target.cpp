#include <string>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#
# @lc app=leetcode id=3734 lang=cpp
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.length();
        vector<int> counts(26, 0);
        for (char c : s) counts[c - 'a']++;

        int odd_count = 0;
        char mid_char = 0;
        vector<int> half_counts(26, 0);
        for (int i = 0; i < 26; ++i) {
            if (counts[i] % 2 != 0) {
                odd_count++;
                mid_char = 'a' + i;
            }
            half_counts[i] = counts[i] / 2;
        }

        if (odd_count > (n % 2)) return "";

        int m = n / 2;
        int k = (n + 1) / 2;

        auto can_form = [&](string prefix) {
            vector<int> temp = half_counts;
            for (char c : prefix) {
                if (temp[c - 'a'] > 0) temp[c - 'a']--;
                else return false;
            }
            return true;
        };

        // Case 1: Prefix matches target for k characters
        if (can_form(target.substr(0, m))) {
            bool match_mid = (n % 2 == 0) || (target[m] == mid_char);
            if (match_mid) {
                string s_half = target.substr(0, m);
                string P = s_half;
                if (n % 2 == 1) P += mid_char;
                reverse(s_half.begin(), s_half.end());
                P += s_half;
                if (P > target) return P;
            }
        }

        // Case 2: Find largest i < k to make P[i] > target[i]
        for (int i = k - 1; i >= 0; --i) {
            if (n % 2 == 1 && i == m) {
                if (mid_char > target[m] && can_form(target.substr(0, m))) {
                    string s_half = target.substr(0, m);
                    string P = s_half + mid_char;
                    reverse(s_half.begin(), s_half.end());
                    P += s_half;
                    return P;
                }
            } else if (i < m) {
                if (can_form(target.substr(0, i))) {
                    vector<int> rem_counts = half_counts;
                    for (int j = 0; j < i; ++j) rem_counts[target[j] - 'a']--;

                    int best_c = -1;
                    for (int c = (target[i] - 'a' + 1); c < 26; ++c) {
                        if (rem_counts[c] > 0) {
                            best_c = c;
                            break;
                        }
                    }

                    if (best_c != -1) {
                        string s_half = target.substr(0, i);
                        s_half += (char)('a' + best_c);
                        rem_counts[best_c]--;
                        for (int c = 0; c < 26; ++c) {
                            while (rem_counts[c] > 0) {
                                s_half += (char)('a' + c);
                                rem_counts[c]--;
                            }
                        }
                        string P = s_half;
                        if (n % 2 == 1) P += mid_char;
                        reverse(s_half.begin(), s_half.end());
                        P += s_half;
                        return P;
                    }
                }
            }
        }

        return "";
    }
};
# @lc code=end