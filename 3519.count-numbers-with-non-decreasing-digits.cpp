#
# @lc app=leetcode id=3519 lang=cpp
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
    int MOD = 1e9 + 7;
    int memo[405][11][2][2];

    // Converts a decimal string to a vector of digits in base b
    vector<int> toBaseB(string s, int b) {
        vector<int> decimal;
        for (char c : s) decimal.push_back(c - '0');
        vector<int> res;
        while (!decimal.empty()) {
            int rem = 0;
            vector<int> next_decimal;
            for (int d : decimal) {
                int cur = d + rem * 10;
                if (!next_decimal.empty() || cur / b > 0) {
                    next_decimal.push_back(cur / b);
                }
                rem = cur % b;
            }
            res.push_back(rem);
            decimal = next_decimal;
        }
        reverse(res.begin(), res.end());
        return res;
    }

    int dfs(const vector<int>& digits, int idx, int last, bool isLess, bool isStarted, int b) {
        if (idx == digits.size()) return isStarted ? 1 : 0;
        if (memo[idx][last][isLess][isStarted] != -1) return memo[idx][last][isLess][isStarted];

        long long ans = 0;
        int limit = isLess ? b - 1 : digits[idx];

        for (int d = 0; d <= limit; ++d) {
            bool nextIsLess = isLess || (d < limit);
            if (!isStarted) {
                // Number hasn't started yet; leading zeros don't count towards non-decreasing constraint
                ans = (ans + dfs(digits, idx + 1, d, nextIsLess, d > 0, b)) % MOD;
            } else if (d >= last) {
                // Number has started; next digit must be >= last digit
                ans = (ans + dfs(digits, idx + 1, d, nextIsLess, true, b)) % MOD;
            }
        }
        return memo[idx][last][isLess][isStarted] = (int)ans;
    }

    int solve(const vector<int>& digits, int b) {
        if (digits.empty()) return 0;
        memset(memo, -1, sizeof(memo));
        return dfs(digits, 0, 0, false, false, b);
    }

    bool check(const vector<int>& digits) {
        for (size_t i = 1; i < digits.size(); ++i) {
            if (digits[i] < digits[i - 1]) return false;
        }
        return !digits.empty();
    }

public:
    int countNumbers(string l, string r, int b) {
        vector<int> digitsR = toBaseB(r, b);
        int ansR = solve(digitsR, b);
        
        vector<int> digitsL = toBaseB(l, b);
        int ansL = solve(digitsL, b);
        
        int res = (ansR - ansL + MOD) % MOD;
        if (check(digitsL)) res = (res + 1) % MOD;
        
        return res;
    }
};
# @lc code=end