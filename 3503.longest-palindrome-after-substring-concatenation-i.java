#
# @lc app=leetcode id=3503 lang=java
#
# [3503] Longest Palindrome After Substring Concatenation I
#
# @lc code=start
class Solution {
    public int longestPalindrome(String s, String t) {
        int maxLen = 0;
        // Check all substrings of s
        for (int i = 0; i <= s.length(); ++i) {
            for (int j = i; j <= s.length(); ++j) {
                String subS = s.substring(i, j);
                // Check all substrings of t
                for (int k = 0; k <= t.length(); ++k) {
                    for (int l = k; l <= t.length(); ++l) {
                        String subT = t.substring(k, l);
                        String concat = subS + subT;
                        if (isPalindrome(concat)) {
                            maxLen = Math.max(maxLen, concat.length());
                        }
                    }
                }
            }
        }
        return maxLen;
    }
    
    private boolean isPalindrome(String str) {
        int left = 0, right = str.length() - 1;
        while (left < right) {
            if (str.charAt(left) != str.charAt(right)) return false;
            left++; right--;
        }
        return true;
    }
}
# @lc code=end