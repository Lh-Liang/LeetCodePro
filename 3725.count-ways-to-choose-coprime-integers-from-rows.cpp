#
# @lc app=leetcode id=3725 lang=cpp
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    int countCoprime(vector<vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        int max_val = 0;
        for (const auto& row : mat) {
            for (int val : row) {
                if (val > max_val) max_val = val;
            }
        }

        if (max_val < 1) return 0;

        // Mobius Sieve
        vector<int> mu(max_val + 1, 0);
        vector<int> primes;
        vector<bool> is_prime(max_val + 1, true);
        mu[1] = 1;
        for (int i = 2; i <= max_val; ++i) {
            if (is_prime[i]) {
                primes.push_back(i);
                mu[i] = -1;
            }
            for (int p : primes) {
                if (1LL * i * p > max_val) break;
                is_prime[i * p] = false;
                if (i % p == 0) {
                    mu[i * p] = 0;
                    break;
                } else {
                    mu[i * p] = -mu[i];
                }
            }
        }

        // Row-wise counts for each possible value
        vector<vector<int>> row_val_counts(m, vector<int>(max_val + 1, 0));
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                row_val_counts[i][mat[i][j]]++;
            }
        }

        long long total_ans = 0;
        const int MOD = 1e9 + 7;

        // Inclusion-Exclusion using Mobius
        for (int g = 1; g <= max_val; ++g) {
            if (mu[g] == 0) continue;

            long long ways_for_g = 1;
            for (int i = 0; i < m; ++i) {
                long long count_mult = 0;
                for (int multiple = g; multiple <= max_val; multiple += g) {
                    count_mult += row_val_counts[i][multiple];
                }
                ways_for_g = (ways_for_g * count_mult) % MOD;
                if (ways_for_g == 0) break;
            }

            if (mu[g] == 1) {
                total_ans = (total_ans + ways_for_g) % MOD;
            } else {
                total_ans = (total_ans - ways_for_g + MOD) % MOD;
            }
        }

        return static_cast<int>(total_ans);
    }
};
# @lc code=end