# @lc app=leetcode id=3519 lang=java
#
# [3519] Count Numbers with Non-Decreasing Digits
#
# @lc code=start
class Solution {
    public int countNumbers(String l, String r, int b) {
        long low = Long.parseLong(l);
        long high = Long.parseLong(r);
        int count = 0;
        int MOD = 1000000007;
        
        for (long num = low; num <= high; num++) {
            if (isNonDecreasingInBase(num, b)) {
                count = (count + 1) % MOD;
            }
        }
        
        return count;
    }
    
    private boolean isNonDecreasingInBase(long num, int base) {
        int prevDigit = -1;
        while (num > 0) {
            int currentDigit = (int)(num % base);
            if (prevDigit != -1 && currentDigit > prevDigit) {
                return false;
            }
            prevDigit = currentDigit;
            num /= base;
        }
        return true;
    }
}
# @lc code=end