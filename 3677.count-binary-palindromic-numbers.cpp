#
# @lc app=leetcode id=3677 lang=cpp
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution {
public:
    int countBinaryPalindromes(long long n) {
        int res = 0;
        int len = 0;
        long long x = n;
        while (x) {
            ++len;
            x >>= 1;
        }
        // Account for n=0
        if (n == 0) return 1;
        // For length from 1 up to len
        for (int l = 1; l <= len; ++l) {
            int half = (l + 1) / 2;
            long long start = 1LL << (half - 1);
            long long end = 1LL << half;
            for (long long left = start; left < end; ++left) {
                long long v = left;
                long long r = left;
                if (l % 2 == 1) r >>= 1;
                // Mirror left to right to form palindrome
                while (r) {
                    v = (v << 1) | (r & 1);
                    r >>= 1;
                }
                if (v <= n) ++res;
            }
        }
        // Add 0
        res += 1;
        return res;
    }
};
# @lc code=end