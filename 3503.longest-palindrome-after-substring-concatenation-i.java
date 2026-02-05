# @lc app=leetcode id=3503 lang=java
#
# [3503] Longest Palindrome After Substring Concatenation I
#
# @lc code=start
class Solution {
    public int longestPalindrome(String s, String t) {
        int maxLen = 0;
        for (int i = 0; i <= s.length(); ++i) {
            for (int j = i; j <= s.length(); ++j) {
                String subS = s.substring(i, j);
                for (int k = 0; k <= t.length(); ++k) {
                    for (int l = k; l <= t.length(); ++l) {
                        String subT = t.substring(k, l);
                        String candidate = subS + subT;
                        if (isPalindrome(candidate)) {
                            maxLen = Math.max(maxLen, candidate.length());
                        }
                    }
                }
            }
        }
        return maxLen;
    }
    private boolean isPalindrome(String s) {
        int left = 0, right = s.length() - 1;
        while (left < right) {
            if (s.charAt(left) != s.charAt(right)) return false;
            ++left; --right;
        }
        return true;
    }
}
# @lc code=end