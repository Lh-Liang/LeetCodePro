#
# @lc app=leetcode id=3519 lang=java
#
# [3519] Count Numbers with Non-Decreasing Digits
#
# @lc code=start
class Solution {
    public int countNumbers(String l, String r, int b) {
        int mod = 1000000007;
        long left = Long.parseLong(l);
        long right = Long.parseLong(r);
        int count = 0;
        for (long num = left; num <= right; num++) {
            if (isNonDecreasing(toBase(num, b))) {
                count = (count + 1) % mod;
            }
        }
        return count;
    }
    
    private List<Integer> toBase(long num, int base) {
        List<Integer> digits = new ArrayList<>();
        while (num > 0) {
            digits.add(0, (int)(num % base));
            num /= base;
        }
        return digits;
    }
    
    private boolean isNonDecreasing(List<Integer> digits) {
        for (int i = 1; i < digits.size(); i++) {
            if (digits.get(i) < digits.get(i - 1)) {
                return false;
            }
        }
        return true;
    }
}
# @lc code=end