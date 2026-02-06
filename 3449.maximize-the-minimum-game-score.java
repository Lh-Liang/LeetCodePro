#
# @lc app=leetcode id=3449 lang=java
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution {
    public long maxScore(int[] points, int m) {
        int n = points.length;
        long left = 0, right = (long)1e15, answer = 0;
        while (left <= right) {
            long mid = left + (right - left) / 2;
            if (canAchieve(points, m, mid)) {
                answer = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return answer;
    }

    private boolean canAchieve(int[] points, int m, long target) {
        long moves = 0;
        for (int p : points) {
            moves += (target + p - 1) / p; // ceil(target/p)
            if (moves > m) return false;
        }
        return moves <= m;
    }
}
# @lc code=end