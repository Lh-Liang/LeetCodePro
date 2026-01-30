#
# @lc app=leetcode id=3677 lang=cpp
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution {
public:
    int countBinaryPalindromes(long long n) {
        if (n == 0) return 1;
        
        long long count = 1; // For n = 0
        
        // Determine the number of bits B in n
        int B = 0;
        long long temp = n;
        while (temp > 0) {
            temp >>= 1;
            B++;
        }
        
        // Count palindromes with length l < B
        for (int l = 1; l < B; ++l) {
            int K = (l + 1) / 2;
            count += (1LL << (K - 1));
        }
        
        // Count palindromes with length B
        int K = (B + 1) / 2;
        long long prefix_n = n >> (B - K);
        long long first_prefix = (1LL << (K - 1));
        
        // All prefixes from first_prefix to prefix_n - 1
        count += (prefix_n - first_prefix);
        
        // Check the palindrome formed by prefix_n itself
        if (constructPalindrome(prefix_n, B) <= n) {
            count++;
        }
        
        return (int)count;
    }

private:
    long long constructPalindrome(long long prefix, int total_len) {
        long long res = prefix;
        int K = (total_len + 1) / 2;
        int bits_to_mirror = total_len / 2;
        
        // We mirror the first 'bits_to_mirror' bits of the prefix in reverse
        // If total_len is even (2K), we mirror all K bits.
        // If total_len is odd (2K-1), we mirror K-1 bits (skipping the middle bit).
        long long mirror_source = (total_len % 2 == 0) ? prefix : (prefix >> 1);
        
        for (int i = 0; i < bits_to_mirror; ++i) {
            res = (res << 1) | (mirror_source & 1);
            mirror_source >>= 1;
        }
        return res;
    }
};
# @lc code=end