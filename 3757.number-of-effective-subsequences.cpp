#
# @lc app=leetcode id=3757 lang=cpp
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
#include <vector>
#include <cmath>

using namespace std;

class Solution {
public:
    int countEffective(vector<int>& nums) {
        const int MOD = 1e9 + 7;
        int n = nums.size();
        int total_or = 0;
        for (int x : nums) total_or |= x;

        if (total_or == 0) return 0;

        // Map bits of total_or to a compact range [0, m-1]
        vector<int> bits;
        for (int i = 0; i < 30; ++i) {
            if ((total_or >> i) & 1) bits.push_back(i);
        }

        int m = bits.size();
        int num_masks = 1 << m;
        vector<int> freq(num_masks, 0);

        for (int x : nums) {
            int mask = 0;
            for (int i = 0; i < m; ++i) {
                if ((x >> bits[i]) & 1) mask |= (1 << i);
            }
            freq[mask]++;
        }

        // SOS DP to find g(mask): number of elements x such that (x_mask & mask) == 0
        // This is equivalent to finding elements whose mask is a subset of (ALL_BITS ^ mask)
        vector<int> subset_sum = freq;
        for (int i = 0; i < m; ++i) {
            for (int mask = 0; mask < num_masks; ++mask) {
                if (mask & (1 << i)) {
                    subset_sum[mask] += subset_sum[mask ^ (1 << i)];
                }
            }
        }

        vector<long long> pow2(n + 1);
        pow2[0] = 1;
        for (int i = 1; i <= n; ++i) pow2[i] = (pow2[i - 1] * 2) % MOD;

        long long ans = 0;
        int ALL_BITS = num_masks - 1;

        for (int mask = 1; mask < num_masks; ++mask) {
            int cnt_bits = __builtin_popcount(mask);
            // Elements x such that x & mask == 0
            int complement_mask = ALL_BITS ^ mask;
            int g_M = subset_sum[complement_mask];
            
            if (cnt_bits % 2 == 1) {
                ans = (ans + pow2[g_M]) % MOD;
            } else {
                ans = (ans - pow2[g_M] + MOD) % MOD;
            }
        }

        return static_cast<int>(ans);
    }
};
# @lc code=end