#
# @lc app=leetcode id=3734 lang=java
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#
# @lc code=start
class Solution {
    public String lexPalindromicPermutation(String s, String target) {
        int n = s.length();
        int[] count = new int[26];
        for (char c : s.toCharArray()) count[c-'a']++;
        int odd = 0;
        char oddChar = 0;
        for (int i = 0; i < 26; i++) {
            if ((count[i] & 1) == 1) {
                odd++; oddChar = (char)('a'+i);
            }
        }
        if ((n & 1) == 0 && odd != 0) return "";
        if ((n & 1) == 1 && odd != 1) return "";
        // build the half and center of the palindrome
        StringBuilder half = new StringBuilder();
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < count[i]/2; j++) half.append((char)('a'+i));
        }
        String center = (n%2==1) ? String.valueOf(oddChar) : "";
        char[] halfArr = half.toString().toCharArray();
        boolean first = true;
        while (true) {
            StringBuilder sb = new StringBuilder();
            sb.append(halfArr);
            sb.append(center);
            for (int i = halfArr.length-1; i >= 0; i--) sb.append(halfArr[i]);
            String palindrome = sb.toString();
            if (palindrome.compareTo(target) > 0) return palindrome;
            // get next permutation for halfArr
            if (!nextPermutation(halfArr)) break;
            first = false;
        }
        return "";
    }
    // Standard next permutation, returns false if already last permutation
    private boolean nextPermutation(char[] arr) {
        int i = arr.length - 2;
        while (i >= 0 && arr[i] >= arr[i+1]) i--;
        if (i < 0) return false;
        int j = arr.length - 1;
        while (arr[j] <= arr[i]) j--;
        char tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
        for (int l = i+1, r = arr.length-1; l < r; l++, r--) {
            tmp = arr[l]; arr[l] = arr[r]; arr[r] = tmp;
        }
        return true;
    }
}
# @lc code=end