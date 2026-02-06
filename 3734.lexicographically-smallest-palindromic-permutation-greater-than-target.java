#
# @lc app=leetcode id=3734 lang=java
#
# [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
#
# @lc code=start
class Solution {
    public String lexPalindromicPermutation(String s, String target) {
        int n = s.length();
        int[] freq = new int[26];
        for (char c : s.toCharArray()) freq[c - 'a']++;
        int odd = 0;
        char oddChar = 0;
        for (int i = 0; i < 26; i++) {
            if (freq[i] % 2 != 0) {
                odd++;
                oddChar = (char)('a' + i);
            }
        }
        if (odd > 1) return "";
        int halfLen = n / 2;
        char[] half = new char[halfLen];
        int idx = 0;
        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < freq[i] / 2; j++) {
                half[idx++] = (char)('a' + i);
            }
        }
        boolean found = false;
        do {
            StringBuilder sb = new StringBuilder();
            sb.append(half);
            if (n % 2 == 1) sb.append(oddChar);
            sb.append(new StringBuilder(new String(half)).reverse());
            String palindrome = sb.toString();
            if (palindrome.compareTo(target) > 0) return palindrome;
        } while (nextPermutation(half));
        return "";
    }
    private boolean nextPermutation(char[] arr) {
        int i = arr.length - 2;
        while (i >= 0 && arr[i] >= arr[i + 1]) i--;
        if (i < 0) return false;
        int j = arr.length - 1;
        while (arr[j] <= arr[i]) j--;
        char tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
        for (int l = i + 1, r = arr.length - 1; l < r; l++, r--) {
            tmp = arr[l]; arr[l] = arr[r]; arr[r] = tmp;
        }
        return true;
    }
}
# @lc code=end