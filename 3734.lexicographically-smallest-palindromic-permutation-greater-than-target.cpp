#
# @lc app=leetcode id=3734 lang=cpp
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#

# @lc code=start
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    string lexPalindromicPermutation(string s, string target) {
        int n = s.length();
        vector<int> counts(26, 0);
        for (char c : s) counts[c - 'a']++;

        int odd_count = 0;
        int mid_idx = -1;
        for (int i = 0; i < 26; ++i) {
            if (counts[i] % 2 == 1) {
                odd_count++;
                mid_idx = i;
            }
        }

        if (odd_count > (n % 2)) return "";

        int m = n / 2;
        vector<int> half_counts(26, 0);
        for (int i = 0; i < 26; ++i) half_counts[i] = counts[i] / 2;

        string mid = "";
        if (n % 2 == 1) mid += (char)('a' + mid_idx);

        string best_p = "";

        // Case A: Match prefix exactly
        bool possible = true;
        vector<int> temp_counts = half_counts;
        for (int i = 0; i < m; ++i) {
            if (--temp_counts[target[i] - 'a'] < 0) {
                possible = false;
                break;
            }
        }
        if (possible) {
            string Q = target.substr(0, m);
            string P = Q + mid;
            string revQ = Q;
            reverse(revQ.begin(), revQ.end());
            P += revQ;
            if (P > target) {
                best_p = P;
            }
        }

        // Case B: Smallest prefix strictly greater than target's first half
        vector<bool> prefix_possible(m + 1, false);
        prefix_possible[0] = true;
        vector<int> p_counts = half_counts;
        for (int i = 0; i < m; ++i) {
            if (--p_counts[target[i] - 'a'] >= 0) {
                prefix_possible[i + 1] = true;
            } else {
                break;
            }
        }

        string candidate2 = "";
        for (int i = m - 1; i >= 0; --i) {
            if (prefix_possible[i]) {
                vector<int> rem_counts = half_counts;
                for (int k = 0; k < i; ++k) rem_counts[target[k] - 'a']--;
                
                int best_char = -1;
                for (int c = (target[i] - 'a' + 1); c < 26; ++c) {
                    if (rem_counts[c] > 0) {
                        best_char = c;
                        break;
                    }
                }

                if (best_char != -1) {
                    string Q = target.substr(0, i);
                    Q += (char)('a' + best_char);
                    rem_counts[best_char]--;
                    for (int c = 0; c < 26; ++c) {
                        while (rem_counts[c] > 0) {
                            Q += (char)('a' + c);
                            rem_counts[c]--;
                        }
                    }
                    string P = Q + mid;
                    string revQ = Q;
                    reverse(revQ.begin(), revQ.end());
                    P += revQ;
                    candidate2 = P;
                    break; 
                }
            }
        }

        if (best_p == "") return candidate2;
        if (candidate2 == "") return best_p;
        return best_p < candidate2 ? best_p : candidate2;
    }
};
# @lc code=end