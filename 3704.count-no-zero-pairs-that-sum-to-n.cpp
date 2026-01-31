#
# @lc app=leetcode id=3704 lang=cpp
#
# [3704] Count No-Zero Pairs That Sum to N
#
# @lc code=start
#include <vector>
#include <string>
#include <cstring>

class Solution {
    long long memo[17][2][2][2];
    std::vector<int> digits;

    long long solve(int idx, int carry, bool ended_a, bool ended_b) {
        if (idx == digits.size()) {
            return (carry == 0) ? 1 : 0;
        }
        if (memo[idx][carry][ended_a][ended_b] != -1) {
            return memo[idx][carry][ended_a][ended_b];
        }

        long long count = 0;
        int target = digits[idx];

        // Try all valid digit pairs (d_a, d_b)
        for (int d_a = 0; d_a <= 9; ++d_a) {
            // Logic for a
            if (idx == 0 && d_a == 0) continue; // Must be positive
            if (ended_a && d_a != 0) continue;   // Once ended, must stay 0
            if (!ended_a && idx > 0 && d_a == 0) {
                // a ends at this index. This is valid for transitions.
            }
            // Note: if !ended_a and d_a is in [1, 9], a remains active.

            for (int d_b = 0; d_b <= 9; ++d_b) {
                // Logic for b
                if (idx == 0 && d_b == 0) continue;
                if (ended_b && d_b != 0) continue;

                int sum = d_a + d_b + carry;
                if (sum % 10 == target) {
                    bool next_ended_a = ended_a || (idx > 0 && d_a == 0);
                    bool next_ended_b = ended_b || (idx > 0 && d_b == 0);
                    count += solve(idx + 1, sum / 10, next_ended_a, next_ended_b);
                }
            }
        }

        return memo[idx][carry][ended_a][ended_b] = count;
    }

public:
    long long countNoZeroPairs(long long n) {
        digits.clear();
        long long temp = n;
        while (temp > 0) {
            digits.push_back(temp % 10);
            temp /= 10;
        }
        // Add one extra digit to catch the final carry if it exists
        digits.push_back(0);

        std::memset(memo, -1, sizeof(memo));
        return solve(0, 0, false, false);
    }
};
# @lc code=end