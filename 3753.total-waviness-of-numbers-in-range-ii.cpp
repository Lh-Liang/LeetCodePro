#
# @lc app=leetcode id=3753 lang=cpp
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
#include <string>
#include <vector>
#include <cstring>
#include <algorithm>

using namespace std;

class Solution {
    struct Result {
        long long totalWaviness;
        long long count;
    };

    string S;
    Result dp[20][11][11][2][2];

    Result solve(int idx, int prev, int prev2, bool isLess, bool isStarted) {
        if (idx == S.size()) {
            return {0, 1};
        }
        if (dp[idx][prev][prev2][isLess][isStarted].count != -1) {
            return dp[idx][prev][prev2][isLess][isStarted];
        }

        long long totW = 0;
        long long cnt = 0;
        int limit = isLess ? 9 : (S[idx] - '0');

        for (int digit = 0; digit <= limit; ++digit) {
            bool newLess = isLess || (digit < limit);
            bool newStarted = isStarted || (digit > 0);

            // Determine contribution of the previous digit (prev)
            // We can only evaluate prev if we have prev2 (meaning prev was not the first digit)
            // and we are currently placing a digit (meaning prev is not the last digit relative to current placement, though we are building prefix)
            int isPeakValley = 0;
            if (isStarted && prev2 != 10) {
                if (prev > prev2 && prev > digit) isPeakValley = 1;
                else if (prev < prev2 && prev < digit) isPeakValley = 1;
            }

            int next_prev = newStarted ? digit : 10;
            int next_prev2 = newStarted ? (isStarted ? prev : 10) : 10;

            Result res = solve(idx + 1, next_prev, next_prev2, newLess, newStarted);
            
            // If we form a valid number suffix (res.count > 0)
            if (res.count > 0) {
                cnt += res.count;
                // Add waviness from the suffix
                totW += res.totalWaviness;
                // Add waviness from the potential peak/valley formed at 'prev'
                // This contribution applies to all valid suffixes formed from the next state
                if (newStarted) { // Only if current digit is part of the number
                     totW += (long long)isPeakValley * res.count;
                }
            }
        }

        return dp[idx][prev][prev2][isLess][isStarted] = {totW, cnt};
    }

    long long calc(long long num) {
        if (num < 0) return 0;
        if (num == 0) return 0; // Problem says num1 >= 1, and 0 has waviness 0 anyway.
        S = to_string(num);
        // Initialize DP table with -1
        // Using a loop or memset carefully. Since struct has longs, memset -1 works if we treat it as bytes, 
        // but safer to loop or use a specific marker. 
        // Actually memset to -1 works for integer types for checking visited if we only check .count
        for(int i=0; i<20; ++i)
            for(int j=0; j<11; ++j)
                for(int k=0; k<11; ++k)
                    for(int l=0; l<2; ++l)
                        for(int m=0; m<2; ++m)
                            dp[i][j][k][l][m] = {-1, -1};

        Result res = solve(0, 10, 10, false, false);
        return res.totalWaviness;
    }

public:
    long long totalWaviness(long long num1, long long num2) {
        return calc(num2) - calc(num1 - 1);
    }
};
# @lc code=end