#
# @lc app=leetcode id=3646 lang=cpp
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
class Solution {
public:
    // Helper to check if a number string is palindrome
    bool isPalindrome(const string& s) {
        int l = 0, r = s.size() - 1;
        while (l < r) {
            if (s[l++] != s[r--]) return false;
        }
        return true;
    }
    // Try possible digit count combinations
    void backtrack(vector<int>& counts, int idx, vector<vector<int>>& combs) {
        if (idx > 9) {
            int total = 0;
            for (int k = 1; k <= 9; ++k) total += counts[k];
            if (total > 0) combs.push_back(counts);
            return;
        }
        // Option: don't use this digit
        counts[idx] = 0; backtrack(counts, idx+1, combs);
        // Option: use this digit exactly idx times
        counts[idx] = idx; backtrack(counts, idx+1, combs);
    }
    // Generate all palindromes from a given digit count
    void buildPalindromes(vector<int>& counts, int len, string& curr, int pos, vector<string>& pals) {
        if (pos >= len/2) {
            string pal = curr;
            if (len % 2) {
                for (int mid = 1; mid <= 9; ++mid) {
                    if (counts[mid] % 2 == 1) {
                        pal[len/2] = '0' + mid;
                        pals.push_back(pal);
                        break;
                    }
                }
            } else pals.push_back(pal);
            return;
        }
        for (int d = 1; d <= 9; ++d) {
            if (counts[d] >= 2) {
                curr[pos] = curr[len-1-pos] = '0' + d;
                counts[d] -= 2;
                buildPalindromes(counts, len, curr, pos+1, pals);
                counts[d] += 2;
            }
        }
    }
    long long specialPalindrome(long long n) {
        vector<vector<int>> combs;
        vector<int> counts(10, 0);
        backtrack(counts, 1, combs);
        long long res = -1;
        for (auto& c : combs) {
            int total = 0, odd = 0;
            for (int k = 1; k <= 9; ++k) {
                total += c[k];
                if (c[k] % 2) ++odd;
            }
            if (odd > 1) continue;
            string curr(total, '0');
            vector<string> pals;
            buildPalindromes(c, total, curr, 0, pals);
            for (auto& s : pals) {
                if (s[0] == '0') continue;
                long long val = stoll(s);
                if (val > n && (res == -1 || val < res)) {
                    res = val;
                }
            }
        }
        return res;
    }
};
# @lc code=end