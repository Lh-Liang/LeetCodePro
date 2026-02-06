#
# @lc app=leetcode id=3646 lang=java
#
# [3646] Next Special Palindrome Number
#

# @lc code=start
class Solution {
    public long specialPalindrome(long n) {
        long candidate = n + 1;
        while (true) {
            candidate = nextPalindrome(candidate);
            if (isSpecial(candidate)) {
                return candidate;
            }
            candidate++; // In case nextPalindrome returned n itself
        }
    }
    
    // Generates the next palindrome >= num
    private long nextPalindrome(long num) {
        String s = Long.toString(num);
        int len = s.length();
        char[] arr = s.toCharArray();
        // Mirror left to right
        for (int i = 0; i < len / 2; i++) {
            arr[len - 1 - i] = arr[i];
        }
        long pal = Long.parseLong(new String(arr));
        if (pal >= num) {
            return pal;
        }
        // Need to increment the middle and mirror again
        int mid = (len - 1) / 2;
        while (mid >= 0 && arr[mid] == '9') {
            arr[mid] = '0';
            arr[len - 1 - mid] = '0';
            mid--;
        }
        if (mid < 0) {
            // All 9's, so next palindrome is 100...001
            StringBuilder sb = new StringBuilder();
            sb.append('1');
            for (int i = 1; i < len; i++) sb.append('0');
            sb.append('1');
            return Long.parseLong(sb.toString());
        }
        arr[mid]++;
        arr[len - 1 - mid] = arr[mid];
        // Mirror again
        for (int i = 0; i < len / 2; i++) {
            arr[len - 1 - i] = arr[i];
        }
        return Long.parseLong(new String(arr));
    }
    
    private boolean isSpecial(long x) {
        int[] freq = new int[10];
        char[] arr = Long.toString(x).toCharArray();
        for (char c : arr) {
            freq[c - '0']++;
        }
        for (int d = 1; d <= 9; d++) {
            if (freq[d] != 0 && freq[d] != d) return false;
        }
        if (freq[0] != 0) return false; // 0 cannot appear since it must appear zero times
        return true;
    }
}
# @lc code=end