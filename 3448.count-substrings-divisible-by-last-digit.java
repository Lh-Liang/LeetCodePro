#
# @lc app=leetcode id=3448 lang=java
#
# [3448] Count Substrings Divisible By Last Digit
#
# @lc code=start
class Solution {
    public long countSubstrings(String s) {
        long count = 0;
        for (int i = 0; i < s.length(); i++) {
            int lastDigit = s.charAt(i) - '0';
            if (lastDigit == 0) continue; // Skip if last digit is zero.
            long number = 0;
            for (int j = i; j >= 0; j--) {
                number = number + (s.charAt(j) - '0') * Math.pow(10, i-j); // Forming number from substring.
                if (number % lastDigit == 0) {
                    count++; // Check divisibility.
                }
            }
        }
        return count;
    }
}
# @lc code=end