#
# @lc app=leetcode id=3677 lang=java
#
# [3677] Count Binary Palindromic Numbers
#
# @lc code=start
class Solution {
    public int countBinaryPalindromes(long n) {
        int count = 0;
        // Special case: 0 is a palindrome
        if (n == 0) return 1;
        int maxBits = Long.toBinaryString(n).length();
        // For each bit length
        for (int l = 1; l <= maxBits; l++) {
            int half = (l + 1) / 2;
            long start = 1L << (half - 1);
            long end = 1L << half;
            for (long firstHalf = start; firstHalf < end; firstHalf++) {
                long palindrome = buildPalindrome(firstHalf, l % 2 == 1);
                if (palindrome <= n) count++;
            }
        }
        return count;
    }
    // Helper to build palindrome from firstHalf. If odd, exclude the middle bit when mirroring
    private long buildPalindrome(long firstHalf, boolean oddLength) {
        long res = firstHalf;
        if (oddLength) firstHalf >>= 1;
        while (firstHalf > 0) {
            res = (res << 1) | (firstHalf & 1);
            firstHalf >>= 1;
        }
        return res;
    }
}
# @lc code=end