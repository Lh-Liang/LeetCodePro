#
# @lc app=leetcode id=3448 lang=java
#
# [3448] Count Substrings Divisible By Last Digit
#
# @lc code=start
class Solution {
    public long countSubstrings(String s) {
        int n = s.length();
        long res = 0;
        for (int i = 0; i < n; ++i) {
            char lastChar = s.charAt(i);
            if (lastChar == '0') continue; // skip if last digit is zero
            int d = lastChar - '0';
            int mod = 0;
            int pow = 1;
            // Check all substrings ending at i
            for (int j = i; j >= 0; --j) {
                int digit = s.charAt(j) - '0';
                mod = (digit * pow + mod) % d;
                if (mod == 0) res++;
                pow = (pow * 10) % d;
                // For efficiency: If pow becomes 0, further digits won't affect mod
                if (pow == 0) break;
            }
        }
        return res;
    }
}
# @lc code=end