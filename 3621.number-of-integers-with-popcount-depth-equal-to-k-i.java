#
# @lc app=leetcode id=3621 lang=java
#
# [3621] Number of Integers With Popcount-Depth Equal to K I
#

# @lc code=start
class Solution {
    public long popcountDepth(long n, int k) {
        long count = 0;
        for (long i = 1; i <= n; i++) {
            int current = (int) i;
            int depth = 0;
            while (current != 1 && depth <= k) {
                current = Integer.bitCount(current);
                depth++;
            }
            if (depth == k && current == 1) {
                count++;
            }
        }
        return count;
    }
}
# @lc code=end