#
# @lc app=leetcode id=3621 lang=cpp
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
#include <vector>
#include <iostream>

class Solution {
public:
    long long popcountDepth(long long n, int k) {
        if (k == 0) return 1; // x = 1 is the only integer with depth 0

        // Precompute combinations nCr
        long long C[64][64];
        for (int i = 0; i < 64; ++i) {
            for (int j = 0; j < 64; ++j) C[i][j] = 0;
            C[i][0] = 1;
            for (int j = 1; j <= i; ++j) {
                C[i][j] = C[i - 1][j - 1] + C[i - 1][j];
            }
        }

        // Precompute depths for all possible popcounts up to 63
        int depth_table[64];
        depth_table[1] = 0; // depth(1) = 0
        for (int i = 2; i < 64; ++i) {
            depth_table[i] = 1 + depth_table[__builtin_popcount(i)];
        }

        // Function to count integers in [1, n] with exactly 'target_bits' set bits
        auto countWithPopcount = [&](long long val, int target_bits) -> long long {
            if (target_bits < 0 || target_bits > 62) return 0;
            long long count = 0;
            int bits_used = 0;
            for (int i = 62; i >= 0; --i) {
                if ((val >> i) & 1) {
                    int remaining_bits = target_bits - bits_used;
                    if (remaining_bits >= 0 && remaining_bits <= i) {
                        count += C[i][remaining_bits];
                    }
                    bits_used++;
                }
            }
            if (bits_used == target_bits) count++;
            return count;
        };

        long long ans = 0;
        // Find all popcounts 'c' such that depth(c) == k - 1
        for (int c = 1; c < 64; ++c) {
            if (depth_table[c] == k - 1) {
                ans += countWithPopcount(n, c);
            }
        }

        // Special adjustment: if k=1, our loop counts x with popcount(x)=1.
        // This includes x=1, but depth(1) is 0, so we exclude it from the k=1 count.
        if (k == 1) ans--;

        return ans;
    }
};
# @lc code=end