#include <bits/stdc++.h>
using namespace std;

// @lc app=leetcode id=3757 lang=cpp
//
// [3757] Number of Effective Subsequences
//

// @lc code=start
class Solution {
public:
    int countEffective(vector<int>& nums) {
        static const int MOD = 1'000'000'007;
        int n = (int)nums.size();

        int T = 0;
        for (int x : nums) T |= x;

        // Collect bit positions that matter (bits set in T)
        vector<int> bits;
        for (int b = 0; b < 31; ++b) {
            if (T & (1 << b)) bits.push_back(b);
        }
        int m = (int)bits.size();
        int fullMask = (1 << m) - 1;

        vector<int> freq(1 << m, 0);
        for (int x : nums) {
            int cm = 0;
            for (int j = 0; j < m; ++j) {
                if (x & (1 << bits[j])) cm |= (1 << j);
            }
            freq[cm]++;
        }

        // SOS DP: G[S] = sum_{M subset of S} freq[M]
        vector<int> G = freq;
        for (int i = 0; i < m; ++i) {
            for (int mask = 0; mask <= fullMask; ++mask) {
                if (mask & (1 << i)) {
                    G[mask] += G[mask ^ (1 << i)];
                }
            }
        }

        // Precompute powers of 2 up to n
        vector<int> pow2(n + 1, 1);
        for (int i = 1; i <= n; ++i) pow2[i] = (pow2[i - 1] * 2LL) % MOD;

        long long ans = 0;
        for (int B = 1; B <= fullMask; ++B) {
            int comp = fullMask ^ B;
            int cnt0 = G[comp];
            long long term = pow2[cnt0];
            int pc = __builtin_popcount((unsigned)B);
            if (pc & 1) ans += term;      // (+) when |B| is odd
            else ans -= term;             // (-) when |B| is even
            ans %= MOD;
        }
        if (ans < 0) ans += MOD;
        return (int)ans;
    }
};
// @lc code=end
