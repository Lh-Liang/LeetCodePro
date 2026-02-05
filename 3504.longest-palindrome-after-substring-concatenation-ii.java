#
# @lc app=leetcode id=3504 lang=java
#
# [3504] Longest Palindrome After Substring Concatenation II
#
# @lc code=start
class Solution {
    public int longestPalindrome(String s, String t) {
        int sLen = s.length(), tLen = t.length();
        int maxLength = 0;
        boolean[][] dpS = new boolean[sLen][sLen];
        boolean[][] dpT = new boolean[tLen][tLen];

        // Precompute palindromic substrings in s
        for (int i = sLen - 1; i >= 0; i--) {
            for (int j = i; j < sLen; j++) {
                if (s.charAt(i) == s.charAt(j) && (j - i < 3 || dpS[i + 1][j - 1])) {
                    dpS[i][j] = true;
                }
            }
        }

        // Precompute palindromic substrings in t
        for (int i = tLen - 1; i >= 0; i--) {
            for (int j = i; j < tLen; j++) {
                if (t.charAt(i) == t.charAt(j) && (j - i < 3 || dpT[i + 1][j - 1])) {
                    dpT[i][j] = true;
                }
            }
        }

        // Check concatenations for longest palindrome length
        for (int i = 0; i < sLen; i++) {
            for (int j = i; j < sLen; j++) {
                if (dpS[i][j]) { // If s[i...j] is a palindrome
                    maxLength = Math.max(maxLength, j - i + 1); // Consider only s part as initial max length
                    String prefix = s.substring(i, j + 1);
                    // Attempt to extend this palindrome with parts of t
                    for (int k = 0; k < tLen; k++) {
                        for (int l = k; l < tLen; l++) {
                            if (dpT[k][l]) { // If t[k...l] is a palindrome, check combined length
                                int lenWithConcat = prefix.length() + l - k + 1;
                                if (isConcatenatedPalindrome(prefix, t.substring(k, l + 1))) { // Check full concatenated string is palindrome via helper method
                                    maxLength = Math.max(maxLength, lenWithConcat);
                                }
                            }
                        }
                    }
                }
            }
        }
        return maxLength;
    }
    
    private boolean isConcatenatedPalindrome(String part1, String part2) { // Optimized check that directly evaluates combined string characteristics 	// Optimized check that directly evaluates combined string characteristics 	// Optimized check that directly evaluates combined string characteristics 	// Optimized check that directly evaluates combined string characteristics 	// Optimized check that directly evaluates combined string characteristics 	// Optimized check that directly evaluates combined string characteristics 	// Optimized check that directly evaluates combined string characteristics{		StringBuilder sb=new StringBuilder(part1).append(part2);		for(int left=0,right=sb.length()-1;left<right;++left,--right){	if(sb.charAt(left)!=sb.charAt(right))return false;}return true;}