#
# @lc app=leetcode id=3753 lang=cpp
#
# [3753] Total Waviness of Numbers in Range II
#

# @lc code=start
#include <string>
#include <vector>
#include <cstring>

using namespace std;

class Solution {
    struct Result {
        long long count;
        long long sum;
    };
    // last and second_last use 10 to represent 'none' or 'placeholder'
    Result memo[20][11][11][2][2];
    int digits[20];
    int len;

    Result dp(int idx, int last, int second_last, bool is_less, bool is_started) {
        if (idx == len) {
            return {1, 0};
        }
        if (memo[idx][last][second_last][is_less][is_started].count != -1) {
            return memo[idx][last][second_last][is_less][is_started];
        }

        Result res = {0, 0};
        int up = is_less ? 9 : digits[idx];

        for (int d = 0; d <= up; ++d) {
            bool next_is_less = is_less || (d < up);
            bool next_is_started = is_started || (d > 0);
            
            int w = 0;
            int next_last, next_second_last;
            
            if (!next_is_started) {
                // Still leading zeros
                next_last = 10;
                next_second_last = 10;
            } else {
                next_last = d;
                if (!is_started) {
                    // This d is the very first digit of the number
                    next_second_last = 10;
                } else {
                    next_second_last = last;
                    // We can only check if 'last' is a peak/valley if 'second_last' exists
                    // and we have a current digit 'd' to act as the right neighbor.
                    if (second_last != 10) {
                        if ((second_last < last && last > d) || (second_last > last && last < d)) {
                            w = 1;
                        }
                    }
                }
            }
            
            Result next_res = dp(idx + 1, next_last, next_second_last, next_is_less, next_is_started);
            res.count += next_res.count;
            res.sum += next_res.sum + (long long)next_res.count * w;
        }

        return memo[idx][last][second_last][is_less][is_started] = res;
    }

    long long solve(long long n) {
        if (n <= 0) return 0;
        string s = to_string(n);
        len = s.length();
        for (int i = 0; i < len; ++i) digits[i] = s[i] - '0';
        
        memset(memo, -1, sizeof(memo));
        
        return dp(0, 10, 10, false, false).sum;
    }

public:
    long long totalWaviness(long long num1, long long num2) {
        return solve(num2) - solve(num1 - 1);
    }
};
# @lc code=end