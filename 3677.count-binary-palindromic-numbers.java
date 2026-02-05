#
# @lc app=leetcode id=3677 lang=java
#
# [3677] Count Binary Palindromic Numbers
#

# @lc code=start
class Solution {
    public long countBinaryPalindromes(long n) {
        long count = 0;
        int maxLen = Long.toBinaryString(n).length();
        // Include 0 in the loop by handling length 1
        for (int len = 1; len <= maxLen; ++len) {
            int halfLen = (len + 1) / 2;
            long start = (len == 1) ? 0 : (1L << (halfLen - 1)); // allow zero for length 1 only
            long end = 1L << halfLen;
            for (long half = start; half < end; ++half) {
                long candidate = buildPalindrome(half, len % 2 == 1);
                if (candidate > n) break;
                count++;
            }
        }
        return count;
    }
    // Helper to build palindrome from half
    private long buildPalindrome(long half, boolean odd) {
        long res = half;
        if (odd) half >>= 1;
        while (half > 0) {
            res = (res << 1) | (half & 1);
            half >>= 1;
        }
        return res;
    }
}
# @lc code=end