#
# @lc app=leetcode id=3677 lang=cpp
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution {
public:
    /**
     * Constructs a binary palindrome of a given length using the provided prefix.
     */
    long long constructPalindrome(long long prefix, int length) {
        long long res = prefix;
        int k = length / 2; // Number of bits to mirror
        long long temp = prefix;
        // If length is odd, the middle bit is not mirrored
        if (length % 2 == 1) {
            temp >>= 1;
        }
        for (int i = 0; i < k; ++i) {
            res = (res << 1) | (temp & 1);
            temp >>= 1;
        }
        return res;
    }

    int countBinaryPalindromes(long long n) {
        if (n == 0) return 1;

        // Find the number of bits in n
        int W = 0;
        long long tempN = n;
        while (tempN > 0) {
            tempN >>= 1;
            W++;
        }

        // Initial count for n=0 ("0") and n=1 ("1")
        long long count = 2;

        // Count all binary palindromes with bit length L such that 2 <= L < W
        for (int L = 2; L < W; ++L) {
            int K = (L + 1) / 2;
            count += (1LL << (K - 1));
        }

        // Count binary palindromes with bit length W that are <= n
        if (W > 1) {
            int K = (W + 1) / 2;
            long long val = n >> (W - K); // The prefix of n that determines the palindrome
            
            // Count palindromes formed by prefixes from 2^(K-1) to val-1
            count += (val - (1LL << (K - 1)));

            // Check if the palindrome formed by the prefix 'val' is <= n
            if (constructPalindrome(val, W) <= n) {
                count++;
            }
        }

        return (int)count;
    }
};
# @lc code=end