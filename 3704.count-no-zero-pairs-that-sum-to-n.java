#
# @lc app=leetcode id=3704 lang=java
#
# [3704] Count No-Zero Pairs That Sum to N
#
# @lc code=start
class Solution {
    public long countNoZeroPairs(long n) {
        long count = 0;
        for (long a = 1; a < n; a++) {
            long b = n - a;
            if (!containsZero(a) && !containsZero(b)) {
                count++;
            }
        }
        return count;
    }
    
    private boolean containsZero(long num) {
        while (num > 0) {
            if (num % 10 == 0) return true;
            num /= 10;
        }
        return false;
    }
}
# @lc code=end