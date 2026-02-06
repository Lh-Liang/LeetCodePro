#
# @lc app=leetcode id=3765 lang=java
#
# [3765] Complete Prime Number
#
# @lc code=start
class Solution {
    private boolean isPrime(int n) {
        if (n < 2) return false;
        if (n == 2) return true;
        if (n % 2 == 0) return false;
        for (int i = 3; i * 1L * i <= n; i += 2) {
            if (n % i == 0) return false;
        }
        return true;
    }

    public boolean completePrime(int num) {
        String s = Integer.toString(num);
        int len = s.length();
        // Check all prefixes
        for (int i = 1; i <= len; i++) {
            int prefix = Integer.parseInt(s.substring(0, i));
            if (!isPrime(prefix)) return false;
        }
        // Check all suffixes
        for (int i = 0; i < len; i++) {
            int suffix = Integer.parseInt(s.substring(i, len));
            if (!isPrime(suffix)) return false;
        }
        return true;
    }
}
# @lc code=end