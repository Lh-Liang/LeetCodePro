#
# @lc app=leetcode id=3449 lang=java
#
# [3449] Maximize the Minimum Game Score
#
# @lc code=start
class Solution {
    public long maxScore(int[] points, int m) {
        int n = points.length;
        long left = 0, right = (long)1e15;
        while (left < right) {
            long mid = right - (right - left) / 2;
            if (canAchieve(points, m, mid)) {
                left = mid;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
    private boolean canAchieve(int[] points, int m, long target) {
        int n = points.length;
        long moves = 0;
        for (int i = 0; i < n; ++i) {
            long need = (target + points[i] - 1) / points[i];
            moves += need;
        }
        // To traverse all indices, need at least n-1 moves (from -1 to 0 to 1 ... n-1)
        moves += n - 1;
        return moves <= m;
    }
}
# @lc code=end