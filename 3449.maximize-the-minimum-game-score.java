#
# @lc app=leetcode id=3449 lang=java
#
# [3449] Maximize the Minimum Game Score
#

# @lc code=start
class Solution {
    public long maxScore(int[] points, int m) {
        int n = points.length;
        long low = 0, high = (long)1e12; // Set initial bounds for binary search
        while (low < high) {
            long mid = (low + high + 1) / 2; // Calculate midpoint, favoring upper bound
            if (canAchieveMin(points, mid, m)) {
                low = mid; // If achievable, try for a higher minimum
            } else {
                high = mid - 1; // If not achievable, reduce upper bound
            }
        }
        return low; // The highest achievable minimum score
    }
    
    private boolean canAchieveMin(int[] points, long minScore, int m) {
        int n = points.length;
        long extraMoves = 0; // Track extra moves needed to achieve minScore at each index
        for (int i = 0; i < n; i++) {
            if (points[i] < minScore) { // If current point is less than minScore
                extraMoves += minScore - points[i]; // Calculate needed moves to reach minScore
                if (extraMoves > m) return false; // If needed moves exceed given moves m, return false
            }
        }
        return true; // If able to achieve at all indices with available moves, return true
    }
}
# @lc code=end