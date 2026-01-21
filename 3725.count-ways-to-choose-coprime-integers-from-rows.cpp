#
# @lc app=leetcode id=3725 lang=cpp
#
# [3725] Count Ways to Choose Coprime Integers from Rows
#

# @lc code=start
class Solution {
public:
    int countCoprime(vector<vector<int>>& mat) {
        const int MOD = 1000000007;
        const int MAXV = 150;
        vector<int> mu(MAXV + 1, 0);
        vector<bool> iscomp(MAXV + 1, false);
        vector<int> primes;
        mu[1] = 1;
        for (int i = 2; i <= MAXV; ++i) {
            if (!iscomp[i]) {
                primes.push_back(i);
                mu[i] = -1;
            }
            for (size_t j = 0; j < primes.size() && 1LL * i * primes[j] <= MAXV; ++j) {
                int p = primes[j];
                iscomp[i * p] = true;
                if (i % p == 0) {
                    mu[i * p] = 0;
                    break;
                } else {
                    mu[i * p] = -mu[i];
                }
            }
        }
        int m = mat.size();
        vector<vector<int>> cnt(m, vector<int>(MAXV + 1, 0));
        for (int r = 0; r < m; ++r) {
            for (int val : mat[r]) {
                for (int d = 1; d * d <= val; ++d) {
                    if (val % d == 0) {
                        cnt[r][d]++;
                        if (d != val / d) {
                            cnt[r][val / d]++;
                        }
                    }
                }
            }
        }
        long long ans = 0;
        for (int d = 1; d <= MAXV; ++d) {
            if (mu[d] == 0) continue;
            long long ways = 1;
            for (int r = 0; r < m; ++r) {
                ways = ways * cnt[r][d] % MOD;
            }
            long long contrib = (mu[d] == 1 ? ways : (MOD - ways) % MOD);
            ans = (ans + contrib) % MOD;
        }
        return ans;
    }
};
# @lc code=end