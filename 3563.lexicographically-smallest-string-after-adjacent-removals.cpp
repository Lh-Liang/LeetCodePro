#
# @lc app=leetcode id=3563 lang=cpp
#
# [3563] Lexicographically Smallest String After Adjacent Removals
#

# @lc code=start
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

class Solution {
public:
    string lexicographicallySmallestString(string s) {
        int n = s.length();
        if (n == 0) return "";

        // canEmpty[i][j] will be true if s[i...j] can be completely removed.
        // We use length + 1 to handle the empty range case easily (e.g. i > j).
        // But indices are 0 to n-1. Let's use specific logic.
        // Initialize with -1 (unknown), 0 (false), 1 (true)
        vector<vector<int>> emptyMemo(n + 1, vector<int>(n + 1, -1));
        
        // dp[i][j] stores the optimal string for s[i...j]
        vector<vector<string>> memo(n + 1, vector<string>(n + 1, ""));
        vector<vector<bool>> visited(n + 1, vector<bool>(n + 1, false));

        return solve(0, n - 1, s, memo, visited, emptyMemo);
    }

private:
    bool isConsecutive(char a, char b) {
        int diff = abs(a - b);
        return diff == 1 || diff == 25;
    }

    // Check if s[i...j] can be reduced to empty string
    bool canEmpty(int i, int j, const string& s, vector<vector<int>>& emptyMemo) {
        if (i > j) return true;
        if ((j - i + 1) % 2 != 0) return false; // Odd length cannot be empty
        if (emptyMemo[i][j] != -1) return emptyMemo[i][j];

        bool res = false;
        // Try to pair s[i] with s[k]
        for (int k = i + 1; k <= j; k += 2) { // k must be at odd distance to have even elements between
            if (isConsecutive(s[i], s[k])) {
                if (canEmpty(i + 1, k - 1, s, emptyMemo) && canEmpty(k + 1, j, s, emptyMemo)) {
                    res = true;
                    break;
                }
            }
        }
        return emptyMemo[i][j] = res;
    }

    string solve(int i, int j, const string& s, vector<vector<string>>& memo, vector<vector<bool>>& visited, vector<vector<int>>& emptyMemo) {
        if (i > j) return "";
        if (visited[i][j]) return memo[i][j];

        // Option 1: Keep s[i]
        string res = s[i] + solve(i + 1, j, s, memo, visited, emptyMemo);

        // Option 2: Remove s[i] by pairing with some s[k]
        // For s[i] and s[k] to be adjacent, s[i+1...k-1] must be fully removable.
        for (int k = i + 1; k <= j; ++k) {
            if (isConsecutive(s[i], s[k])) {
                if (canEmpty(i + 1, k - 1, s, emptyMemo)) {
                    // If valid, we are left with s[k+1...j]
                    string candidate = solve(k + 1, j, s, memo, visited, emptyMemo);
                    if (candidate < res) {
                        res = candidate;
                    }
                }
            }
        }

        visited[i][j] = true;
        memo[i][j] = res;
        return res;
    }
};
# @lc code=end