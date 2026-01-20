#
# @lc app=leetcode id=3621 lang=cpp
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
class Solution {
public:
    long long combinations[65][65];

    void initCombinations() {
        for (int i = 0; i <= 64; i++) {
            combinations[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                combinations[i][j] = combinations[i - 1][j - 1] + combinations[i - 1][j];
            }
        }
    }

    long long countWithSetBits(long long n, int k) {
        if (k < 0) return 0;
        long long ans = 0;
        int current_set_bits = 0;
        
        // We consider bits from 62 down to 0 (since n <= 10^15 < 2^60)
        for (int i = 62; i >= 0; i--) {
            if ((n >> i) & 1) {
                // If the current bit of n is 1, we can either:
                // 1. Put 0 here. Then we have 'i' remaining positions to fill.
                //    We need to choose (k - current_set_bits) bits.
                int needed = k - current_set_bits;
                if (needed >= 0 && needed <= i) {
                    ans += combinations[i][needed];
                }
                // 2. Put 1 here. This matches n's bit. Increment count and proceed.
                current_set_bits++;
            }
        }
        // Check if n itself has exactly k bits
        if (current_set_bits == k) {
            ans++;
        }
        return ans;
    }

    long long popcountDepth(long long n, int k) {
        if (k == 0) return 1; // Only number 1 has depth 0, assuming range [1, n] covers 1.
                              // Wait, definition: p0 = x. Depth is smallest d such that pd = 1.
                              // If x=1, p0=1, depth=0. So if n>=1, ans is 1.
                              // But wait, the example says x=2 -> 1 (depth 1), x=4 -> 1 (depth 1).
                              // x=1 -> 1 (depth 0).
                              // The problem asks for range [1, n].
                              // If k=0, we need x in [1, n] such that depth is 0. Only x=1 works.
                              // So if n >= 1 return 1, else 0.
        
        initCombinations();

        // Precompute depths for small numbers (popcounts)
        // Max n is 10^15, which is less than 2^50. Max popcount is around 50.
        // Let's go up to 64 just to be safe.
        int depth[65];
        depth[1] = 0;
        for (int i = 2; i <= 64; i++) {
            depth[i] = 1 + depth[__builtin_popcount(i)];
        }

        long long total = 0;
        
        // We are looking for x in [1, n] such that depth(x) == k.
        // depth(x) = 1 + depth(popcount(x)).
        // So we need 1 + depth(popcount(x)) == k => depth(popcount(x)) == k - 1.
        // Let c = popcount(x). We need c such that depth[c] == k - 1.
        // c can range from 1 to 60 (approx).

        for (int c = 1; c <= 60; c++) {
            if (depth[c] == k - 1) {
                // We need to count integers in [1, n] with exactly c set bits.
                total += countWithSetBits(n, c);
            }
        }

        return total;
    }
};
# @lc code=end