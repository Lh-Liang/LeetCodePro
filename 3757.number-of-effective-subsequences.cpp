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
        int total_or = 0;
        for (int x : nums) total_or |= x;
        // For each bit in total_or, collect indices that provide that bit
        int maxbit = 0;
        for (int i = 0; i < 21; ++i) if (total_or & (1 << i)) maxbit = i;
        // For each element, record its mask relative to total_or
        vector<int> mask(n, 0);
        for (int i = 0; i < n; ++i) {
            mask[i] = nums[i] & total_or;
        }
        // For each bit, count how many numbers have that bit
        vector<int> bit_count(21, 0);
        for (int i = 0; i < n; ++i)
            for (int b = 0; b < 21; ++b)
                if ((total_or & (1 << b)) && (nums[i] & (1 << b)))
                    bit_count[b]++;
        // Find indices that are the only contributor to some bit
        set<int> critical;
        for (int b = 0; b < 21; ++b) {
            if ((total_or & (1 << b)) && bit_count[b] == 1) {
                // Find which index
                for (int i = 0; i < n; ++i)
                    if (nums[i] & (1 << b))
                        critical.insert(i);
            }
        }
        // The minimum set to remove to strictly decrease OR is all critical indices
        int critical_cnt = critical.size();
        if (critical_cnt == 0) return 0;
        // All supersets of critical indices are effective
        // For the rest (n - critical_cnt), each can be included or not
        long long ans = 1;
        for (int i = 0; i < n - critical_cnt; ++i) ans = ans * 2 % MOD;
        // Exclude the empty set (must remove at least the criticals)
        return ans % MOD;
    }
};
# @lc code=end