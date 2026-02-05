#
# @lc app=leetcode id=3734 lang=java
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#
# @lc code=start
class Solution {
    public String lexPalindromicPermutation(String s, String target) {
        int[] count = new int[26];
        for (char c : s.toCharArray()) {
            count[c - 'a']++;
        }
        StringBuilder half = new StringBuilder();
        char oddChar = 0;
        for (int i = 0; i < 26; i++) {
            if (count[i] % 2 == 1) {
                if (oddChar != 0) return ""; // More than one odd character, can't be palindromic
                oddChar = (char)(i + 'a');
            }
            for (int j = 0; j < count[i] / 2; j++) {
                half.append((char)(i + 'a'));
            }
        }
        char[] halfArray = half.toString().toCharArray();
        Arrays.sort(halfArray);
        do {
            StringBuilder palindrome = new StringBuilder(new String(halfArray));
            if (oddChar != 0) palindrome.append(oddChar);
            palindrome.append(new StringBuilder(new String(halfArray)).reverse());
            if (palindrome.toString().compareTo(target) > 0) return palindrome.toString();
        } while (nextPermutation(halfArray)); // Find next permutation that is greater than current one. 
        return ""; // No valid permutation found. 
    } 
    private boolean nextPermutation(char[] array) { 
        int i = array.length - 2; 
        while (i >= 0 && array[i] >= array[i + 1]) i--; 
        if (i < 0) return false; // No next permutation possible. 
        int j = array.length - 1; 
        while (array[j] <= array[i]) j--; 
        swap(array, i, j); 
        reverse(array, i + 1); 
        return true; 
    } 
    private void swap(char[] array, int i, int j) { 
       char temp = array[i]; array[i] = array[j]; array[j] = temp; 
    } 	private void reverse(char[] array, int start) { 		int end = array.length - 1;		while(start < end){ swap(array,start++,end--);} } } # @lc code=end