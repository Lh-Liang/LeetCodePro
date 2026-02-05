#
# @lc app=leetcode id=3782 lang=java
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#
# @lc code=start
class Solution {
    public long lastInteger(long n) {
        long res = 1;
        boolean left = true;
        long step = 1, remain = n;
        while (remain > 1) {
            if (left || remain % 2 == 1) {
                res += step;
            }
            step *= 2;
            remain /= 2;
            left = !left;
        }
        return res;
    }
}
# @lc code=end