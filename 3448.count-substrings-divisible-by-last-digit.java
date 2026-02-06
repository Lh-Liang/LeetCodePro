#
# @lc app=leetcode id=3448 lang=java
#
# [3448] Count Substrings Divisible By Last Digit
#
# @lc code=start
class Solution {
    public long countSubstrings(String s) {
        int n = s.length();
        long ans = 0;
        for (int i = 0; i < n; ++i) {
            char ch = s.charAt(i);
            if (ch == '0') continue; // last digit must be non-zero
            int d = ch - '0';
            // Single digit substrings
            ans++;
            int rem = 0;
            int pow = 1;
            // Go backwards and check all substrings ending at i
            for (int j = i - 1; j >= 0; --j) {
                rem = ( (s.charAt(j) - '0') * pow + rem ) % d;
                pow = (pow * 10) % d;
                if (rem == 0) ans++;
            }
        }
        return ans;
    }
}
# @lc code=end