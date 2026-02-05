#
# @lc app=leetcode id=3677 lang=java
#
# [3677] Count Binary Palindromic Numbers
#
# @lc code=start
class Solution {
    public int countBinaryPalindromes(long n) {
        int count = 0;
        int maxLength = Long.toBinaryString(n).length();
        
        // Generate palindromes for each possible bit length
        for (int len = 1; len <= maxLength; len++) {
            // Generate palindromes with 'len' bits
            count += generatePalindromes(len, n);
        }
        return count;
    }
    
    private int generatePalindromes(int length, long n) {
        int halfLength = (length + 1) / 2;
        int start = 1 << (halfLength - 1); // Start with smallest half palindrome of this length
        int end = (1 << halfLength); // End with largest half palindrome of this length
        int count = 0;
        
        for (int i = start; i < end; i++) {
            long palindrome = createPalindrome(i, length % 2 == 0);
            if (palindrome <= n) {
                count++;
            }
        }
        return count;
    }
    
    private long createPalindrome(int half, boolean evenLength) {
        long result = half;
        if (!evenLength) {
            half >>= 1; // Remove the middle bit for odd length
        }
        while (half > 0) {
            result = (result << 1) | (half & 1);
            half >>= 1;
        }
        return result;
    }
}
# @lc code=end