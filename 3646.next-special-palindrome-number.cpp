#
# @lc app=leetcode id=3646 lang=cpp
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
#include <vector>
#include <string>
#include <set>
#include <algorithm>
using namespace std;
class Solution {
public:
    // Check if a digit profile can form a palindrome
    bool canFormPalindrome(const vector<int>& counts) {
        int odd = 0, len = 0;
        for (int k = 0; k < 9; ++k) {
            if (counts[k] % 2) ++odd;
            len += counts[k];
        }
        if (len == 0) return false;
        if (len % 2 == 0) return odd == 0;
        else return odd == 1;
    }
    // Generate all unique permutations of half, using std::next_permutation
    void generateUniqueHalves(vector<int>& half, set<vector<int>>& uniqueHalves) {
        sort(half.begin(), half.end());
        do {
            if (half.empty() || half[0] != 0)  // Avoid leading zeros
                uniqueHalves.insert(half);
        } while (next_permutation(half.begin(), half.end()));
    }
    // Build unique palindromic numbers for a given digit profile
    void buildUniquePalindromes(const vector<int>& counts, long long n, long long& best) {
        vector<int> half;
        int center = -1;
        for (int k = 0; k < 9; ++k) {
            if (counts[k] % 2) center = k + 1;
            for (int i = 0; i < counts[k] / 2; ++i) half.push_back(k + 1);
        }
        set<vector<int>> uniqueHalves;
        generateUniqueHalves(half, uniqueHalves);
        for (const auto& h : uniqueHalves) {
            string s;
            for (int d : h) s += (char)('0' + d);
            string rev_s(s.rbegin(), s.rend());
            if (center != -1) s += (char)('0' + center);
            s += rev_s;
            if (s.empty() || s[0] == '0') continue; // Universal leading zero check
            // Explicitly verify all digit frequency constraints
            vector<int> digitCount(10, 0);
            for (char c : s) digitCount[c - '0']++;
            bool valid = true;
            for (int d = 1; d <= 9; ++d) {
                if (digitCount[d] && digitCount[d] != d) {
                    valid = false;
                    break;
                }
            }
            if (!valid) continue;
            long long val = stoll(s);
            if (val > n && (best == -1 || val < best)) best = val;
        }
    }
    // Recursively build all valid profiles
    void dfs(vector<int>& counts, int pos, vector<vector<int>>& profiles) {
        if (pos == 9) {
            if (canFormPalindrome(counts)) profiles.push_back(counts);
            return;
        }
        counts[pos] = 0;
        dfs(counts, pos + 1, profiles);
        counts[pos] = pos + 1;
        dfs(counts, pos + 1, profiles);
    }
    long long specialPalindrome(long long n) {
        vector<vector<int>> profiles;
        vector<int> counts(9, 0);
        dfs(counts, 0, profiles);
        long long best = -1;
        for (const auto& prof : profiles) {
            buildUniquePalindromes(prof, n, best);
        }
        return best;
    }
};
# @lc code=end