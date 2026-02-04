#
# @lc app=leetcode id=3757 lang=cpp
#
# [3757] Number of Effective Subsequences
#

# @lc code=start
class Solution {
public:
    int countEffective(vector<int>& nums) {
        const int MOD = 1e9 + 7;
        int n = nums.size();
        int full_or = 0;
        for (int num : nums) full_or |= num;
        // Find which bits are set in full_or
        vector<int> bits;
        for (int b = 0; b < 21; ++b) if (full_or & (1 << b)) bits.push_back(b);
        int m = bits.size();
        // For each bit, collect the elements that set it
        vector<vector<int>> bit_sets(m);
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < m; ++j) {
                if (nums[i] & (1 << bits[j])) bit_sets[j].push_back(i);
            }
        }
        // Inclusion-exclusion over non-empty subsets of set bits
        long long ans = 0;
        for (int mask = 1; mask < (1 << m); ++mask) {
            vector<bool> covered(n, false);
            int cnt = 0;
            for (int j = 0; j < m; ++j) {
                if (mask & (1 << j)) {
                    for (int idx : bit_sets[j]) {
                        if (!covered[idx]) {
                            covered[idx] = true;
                            ++cnt;
                        }
                    }
                }
            }
            // For this subset of bits, count all non-empty subsets of contributors
            long long way = (1LL << cnt) - 1; // 2^cnt - 1
            // Inclusion-exclusion: add if odd, subtract if even number of bits in mask
            if (__builtin_popcount(mask) % 2 == 1)
                ans = (ans + way) % MOD;
            else
                ans = (ans - way + MOD) % MOD;
        }
        return (int)ans;
    }
};
# @lc code=end