#
# @lc app=leetcode id=3677 lang=cpp
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution {
public:
    long long countBinaryPalindromes(long long n) {
        long long res = 0;
        // Step 1: Explicitly include 0 if n >= 0
        if (n >= 0) res = 1;
        // Step 2: Determine max bit length
        int maxLen = 0;
        long long tmp = n;
        while (tmp) {
            maxLen++;
            tmp >>= 1;
        }
        // Step 3: Generate candidates by bit length
        for (int len = 1; len <= maxLen; ++len) {
            int half = (len + 1) / 2;
            long long start = 1LL << (half - 1);
            long long end = 1LL << half;
            for (long long i = start; i < end; ++i) {
                long long pal = i;
                // Step 4: Mirror to form full palindrome
                for (int j = (len % 2 ? half - 2 : half - 1); j >= 0; --j) {
                    pal = (pal << 1) | ((i >> j) & 1);
                }
                // Step 5: Verify candidate is within range and palindromic
                if (pal <= n) {
                    res++;
                }
            }
        }
        // Step 6: All variables/return types use long long to avoid overflow
        return res;
    }
};
# @lc code=end