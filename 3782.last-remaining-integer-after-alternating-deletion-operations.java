# \ @lc app=leetcode id=3782 lang=java
# \ [3782] Last Remaining Integer After Alternating Deletion Operations
#
# \ @lc code=start
class Solution {
    public long lastInteger(long n) {
        long start = 1;
        long step = 1;
        boolean leftToRight = true;
        while (n > 1) {
            if (leftToRight || n % 2 == 1) {
                start += step;
            }
            n /= 2;
            step *= 2;
            leftToRight = !leftToRight;
        }
        return start;
    }
}
# \ @lc code=end