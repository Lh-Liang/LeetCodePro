#
# @lc app=leetcode id=3704 lang=cpp
#
# [3704] Count No-Zero Pairs That Sum to N
#

# @lc code=start
#include <vector>
#include <string>
#include <algorithm>
#include <iostream>
#include <cstring>

using namespace std;

class Solution {
    long long memo[18][2][2][2];
    vector<int> digits;

    long long solve(int idx, int carry, int state_a, int state_b) {
        if (idx == 17) {
            return (carry == 0 && state_a == 1 && state_b == 1) ? 1 : 0;
        }
        if (memo[idx][carry][state_a][state_b] != -1) {
            return memo[idx][carry][state_a][state_b];
        }

        long long count = 0;
        vector<int> allowed_a, allowed_b;

        if (state_a == 0) {
            for (int d = 1; d <= 9; ++d) allowed_a.push_back(d);
        } else {
            allowed_a.push_back(0);
        }

        if (state_b == 0) {
            for (int d = 1; d <= 9; ++d) allowed_b.push_back(d);
        } else {
            allowed_b.push_back(0);
        }

        int target = digits[idx];

        for (int va : allowed_a) {
            for (int vb : allowed_b) {
                int current_sum = va + vb + carry;
                if (current_sum % 10 == target) {
                    int next_carry = current_sum / 10;
                    
                    int next_states_a[2], next_states_b[2];
                    int num_nsa = 0, num_nsb = 0;

                    if (state_a == 0) {
                        next_states_a[num_nsa++] = 0;
                        next_states_a[num_nsa++] = 1;
                    } else {
                        next_states_a[num_nsa++] = 1;
                    }

                    if (state_b == 0) {
                        next_states_b[num_nsb++] = 0;
                        next_states_b[num_nsb++] = 1;
                    } else {
                        next_states_b[num_nsb++] = 1;
                    }

                    for (int i = 0; i < num_nsa; ++i) {
                        for (int j = 0; j < num_nsb; ++j) {
                            count += solve(idx + 1, next_carry, next_states_a[i], next_states_b[j]);
                        }
                    }
                }
            }
        }

        return memo[idx][carry][state_a][state_b] = count;
    }

public:
    long long countNoZeroPairs(long long n) {
        digits.clear();
        long long temp = n;
        for (int i = 0; i < 17; ++i) {
            digits.push_back(temp % 10);
            temp /= 10;
        }
        memset(memo, -1, sizeof(memo));
        return solve(0, 0, 0, 0);
    }
};
# @lc code=end