#
# @lc app=leetcode id=3765 lang=java
#
# [3765] Complete Prime Number
#
# @lc code=start
class Solution {
    public boolean completePrime(int num) {
        if (num < 2) return false;
        String s = Integer.toString(num);
        int n = s.length();
        // Check all prefixes
        for (int i = 1; i <= n; ++i) {
            int prefix = Integer.parseInt(s.substring(0, i));
            if (!isPrime(prefix)) return false;
        }
        // Check all suffixes
        for (int i = 0; i < n; ++i) {
            int suffix = Integer.parseInt(s.substring(i, n));
            if (!isPrime(suffix)) return false;
        }
        return true;
    }
    private boolean isPrime(int num) {
        if (num < 2) return false;
        if (num == 2) return true;
        if (num % 2 == 0) return false;
        for (int i = 3; i * i <= num; i += 2) {
            if (num % i == 0) return false;
        }
        return true;
    }
}
# @lc code=end