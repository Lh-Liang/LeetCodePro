#include <vector>

using namespace std;

#
# @lc app=leetcode id=3725 lang=cpp
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
class Solution {
public:
    /**
     * Returns the number of ways to choose exactly one integer from each row 
     * such that the GCD of all chosen integers is 1.
     */
    int countCoprime(vector<vector<int>>& mat) {
        int m = mat.size();
        if (m == 0) return 0;
        int n = mat[0].size();
        
        int max_v = 0;
        for (const auto& row : mat) {
            for (int x : row) {
                if (x > max_v) max_v = x;
            }
        }

        if (max_v == 0) return 0;

        // Step 1: Precompute the Mobius function up to max_v using a linear sieve
        vector<int> mu(max_v + 1, 0);
        vector<int> primes;
        vector<bool> is_not_prime(max_v + 1, false);
        mu[1] = 1;
        for (int i = 2; i <= max_v; ++i) {
            if (!is_not_prime[i]) {
                primes.push_back(i);
                mu[i] = -1;
            }
            for (int p : primes) {
                if (i * p > max_v) break;
                is_not_prime[i * p] = true;
                if (i % p == 0) {
                    mu[i * p] = 0;
                    break;
                } else {
                    mu[i * p] = -mu[i];
                }
            }
        }

        // Step 2: Pre-count the frequency of each value in each row
        vector<vector<int>> val_counts(m, vector<int>(max_v + 1, 0));
        for (int i = 0; i < m; ++i) {
            for (int x : mat[i]) {
                val_counts[i][x]++;
            }
        }

        long long total_ans = 0;
        const long long MOD = 1e9 + 7;

        // Step 3: Use Mobius Inversion to find the number of ways where GCD is 1
        // f(1) = sum over g of (mu(g) * F(g))
        // F(g) is the number of ways to pick integers all divisible by g
        for (int g = 1; g <= max_v; ++g) {
            if (mu[g] == 0) continue;

            long long ways_for_g = 1;
            for (int i = 0; i < m; ++i) {
                int count_multiples = 0;
                for (int multiple = g; multiple <= max_v; multiple += g) {
                    count_multiples += val_counts[i][multiple];
                }
                // Multiply the number of choices in this row that are multiples of g
                ways_for_g = (ways_for_g * count_multiples) % MOD;
                if (ways_for_g == 0) break;
            }

            if (mu[g] == 1) {
                total_ans = (total_ans + ways_for_g) % MOD;
            } else if (mu[g] == -1) {
                total_ans = (total_ans - ways_for_g + MOD) % MOD;
            }
        }

        return static_cast<int>(total_ans);
    }
};
# @lc code=end