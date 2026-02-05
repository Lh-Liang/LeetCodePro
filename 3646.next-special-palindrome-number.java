#
# @lc app=leetcode id=3646 lang=java
#
# [3646] Next Special Palindrome Number
#
# @lc code=start
class Solution {
    // Helper to check if a string is a palindrome
    private boolean isPalindrome(String s) {
        int l = 0, r = s.length() - 1;
        while (l < r) {
            if (s.charAt(l++) != s.charAt(r--)) return false;
        }
        return true;
    }
    // Helper to count digit frequencies
    private int[] countDigits(String s) {
        int[] count = new int[10];
        for (char c : s.toCharArray()) count[c - '0']++;
        return count;
    }
    // Helper to check the special property
    private boolean isSpecial(int[] count) {
        for (int d = 0; d <= 9; ++d) {
            if (count[d] != 0 && count[d] != d) return false;
        }
        return true;
    }
    // Generate palindromes of given length recursively, no early pruning on partial candidates
    private void generatePalindromes(int pos, char[] curr, int len, long limit, long[] result) {
        if (result[0] != -1) return; // already found
        if (pos >= (len + 1) / 2) {
            String s = new String(curr);
            long val = Long.parseLong(s);
            if (val > limit) {
                int[] count = countDigits(s);
                if (isPalindrome(s) && isSpecial(count)) {
                    result[0] = val;
                }
            }
            return;
        }
        for (char d = (pos == 0 ? '1' : '0'); d <= '9'; ++d) {
            curr[pos] = d;
            curr[len - 1 - pos] = d;
            generatePalindromes(pos + 1, curr, len, limit, result);
            if (result[0] != -1) return;
        }
    }
    public long specialPalindrome(long n) {
        String nStr = Long.toString(n + 1);
        int minLen = nStr.length();
        int maxLen = 18;
        for (int len = minLen; len <= maxLen; ++len) {
            char[] curr = new char[len];
            long[] result = new long[]{-1};
            generatePalindromes(0, curr, len, n, result);
            if (result[0] != -1) return result[0];
        }
        return -1;
    }
}
# @lc code=end