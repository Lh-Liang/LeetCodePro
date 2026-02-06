#
# @lc app=leetcode id=3782 lang=java
#
# [3782] Last Remaining Integer After Alternating Deletion Operations
#
# @lc code=start
class Solution {
    public long lastInteger(long n) {
        long head = 1;
        long step = 1;
        boolean left = true;
        while (n > 1) {
            if (left || n % 2 == 1) {
                head += step;
            }
            step <<= 1;
            n >>= 1;
            left = !left;
        }
        return head;
    }
}
# @lc code=end