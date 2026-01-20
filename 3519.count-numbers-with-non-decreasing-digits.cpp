#
# @lc app=leetcode id=3519 lang=cpp
#
# [3519] Count Numbers with Non-Decreasing Digits
#

# @lc code=start
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <cstring>

using namespace std;

class Solution {
    long long memo[110][11][2][2];
    int MOD = 1e9 + 7;
    int B;

    // Converts a base-10 string to a base-B vector of digits
    vector<int> toBaseB(string s, int b) {
        vector<int> decimalDigits;
        for (char c : s) decimalDigits.push_back(c - '0');

        vector<int> baseBDigits;
        while (!decimalDigits.empty()) {
            long long remainder = 0;
            vector<int> nextDecimal;
            bool leadingZeros = true;
            for (int digit : decimalDigits) {
                long long current = remainder * 10 + digit;
                int quotient = current / b;
                remainder = current % b;
                if (quotient > 0 || !leadingZeros) {
                    nextDecimal.push_back(quotient);
                    leadingZeros = false;
                }
            }
            baseBDigits.push_back(remainder);
            decimalDigits = nextDecimal;
        }
        reverse(baseBDigits.begin(), baseBDigits.end());
        if (baseBDigits.empty()) return {0};
        return baseBDigits;
    }

    // Decrements the number represented by the base-B vector
    void decrement(vector<int>& num) {
        int n = num.size();
        int i = n - 1;
        while (i >= 0) {
            if (num[i] > 0) {
                num[i]--;
                break;
            } else {
                num[i] = B - 1;
                i--;
            }
        }
        // Remove leading zero if the number shrinks, unless it becomes just [0]
        if (num.size() > 1 && num[0] == 0) {
            num.erase(num.begin());
        }
    }

    long long dp(int idx, int lastVal, bool isLimit, bool isStarted, const vector<int>& digits) {
        if (idx == digits.size()) {
            return 1;
        }
        if (memo[idx][lastVal][isLimit][isStarted] != -1) {
            return memo[idx][lastVal][isLimit][isStarted];
        }

        long long ans = 0;
        int up = isLimit ? digits[idx] : (B - 1);

        for (int d = 0; d <= up; ++d) {
            if (!isStarted) {
                if (d == 0) {
                    // Still haven't started (leading zeros)
                    ans = (ans + dp(idx + 1, 0, isLimit && (d == up), false, digits)) % MOD;
                } else {
                    // Starting now, d > 0
                    ans = (ans + dp(idx + 1, d, isLimit && (d == up), true, digits)) % MOD;
                }
            } else {
                // Already started, must maintain non-decreasing order
                if (d >= lastVal) {
                    ans = (ans + dp(idx + 1, d, isLimit && (d == up), true, digits)) % MOD;
                }
            }
        }

        return memo[idx][lastVal][isLimit][isStarted] = ans;
    }

    long long solve(vector<int>& digits) {
        memset(memo, -1, sizeof(memo));
        // Special case: The DP counts 0 as a valid number implicitly if we consider the "empty" non-started path
        // resolving to 1 at the end. However, the problem range is inclusive.
        // The DP state `isStarted=false` reaching the end essentially counts the number 0.
        // If the number is effectively 0 (vector is {0}), the logic should hold.
        return dp(0, 0, true, false, digits);
    }

public:
    int countNumbers(string l, string r, int b) {
        B = b;
        vector<int> rDigits = toBaseB(r, b);
        vector<int> lDigits = toBaseB(l, b);
        
        // We want range [l, r], so we calculate solve(r) - solve(l - 1).
        decrement(lDigits);
        
        long long ansR = solve(rDigits);
        long long ansL = solve(lDigits);
        
        return (ansR - ansL + MOD) % MOD;
    }
};
# @lc code=end