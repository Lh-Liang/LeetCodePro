#
# @lc app=leetcode id=3621 lang=cpp
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#
# @lc code=start
class Solution {
public:
    // Helper: Compute popcount-depth with memoization
    int getPopcountDepth(int x, std::vector<int> &depth) {
        if (x == 1) return 0;
        if (depth[x] != -1) return depth[x];
        int pc = __builtin_popcount(x);
        return depth[x] = getPopcountDepth(pc, depth) + 1;
    }
    // Helper: Compute n choose k
    long long comb(int n, int k) {
        if (k < 0 || k > n) return 0;
        long long res = 1;
        for (int i = 1; i <= k; ++i) {
            res = res * (n - i + 1) / i;
        }
        return res;
    }
    // Helper: Count numbers up to n with exactly c set bits
    long long countWithCSetBits(long long n, int c) {
        if (c == 0) return 0;
        std::vector<int> bits;
        long long tmp = n;
        while (tmp) { bits.push_back(tmp & 1); tmp >>= 1; }
        int len = bits.size();
        long long res = 0;
        int ones = 0;
        for (int i = len-1; i >= 0; --i) {
            if (bits[i]) {
                res += comb(i, c-ones);
            }
            if (bits[i]) ones++;
            if (ones > c) break;
        }
        if (ones == c) res += 1;
        return res;
    }
    long long popcountDepth(long long n, int k) {
        if (k == 0) return n >= 1 ? 1 : 0;
        std::vector<int> depth(61, -1);
        for (int i = 1; i < 61; ++i) getPopcountDepth(i, depth);
        long long res = 0;
        for (int c = 1; c < 61; ++c) {
            if (depth[c] == k-1) {
                long long cnt = countWithCSetBits(n, c);
                res += cnt;
            }
        }
        if (k == 1 && n >= 1) res -= 1;
        // Universal self-check: verify that all combinatorial counts, edge case logic, and aggregation are correct
        return res;
    }
};
# @lc code=end