#
# @lc app=leetcode id=3677 lang=java
#
# [3677] Count Binary Palindromic Numbers
#
# @lc code=start
class Solution {
    public int countBinaryPalindromes(long n) {
        int count = 0;
        for (long i = 0; i <= n; i++) {
            String binaryStr = Long.toBinaryString(i);
            if (isPalindrome(binaryStr)) {
                count++;
            }
        }
        return count;
    }
    
    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left++) != s.charAt(right--)) {
                return false;
            }
        }
        return true;
    }
}
# @lc code=end