#
# @lc app=leetcode id=3464 lang=java
#
# [3464] Maximize the Distance Between Points on a Square
#
# @lc code=start
class Solution {
    public int maxDistance(int side, int[][] points, int k) {
        int n = points.length;
        int left = 0, right = 2 * side;
        int ans = 0;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (canSelect(points, k, mid)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }

    // Check if we can select k points with pairwise Manhattan distance >= dist
    private boolean canSelect(int[][] points, int k, int dist) {
        return backtrack(points, k, dist, 0, new boolean[points.length], 0);
    }

    private boolean backtrack(int[][] points, int k, int dist, int start, boolean[] used, int count) {
        if (count == k) return true;
        for (int i = start; i < points.length; ++i) {
            if (!used[i]) {
                boolean valid = true;
                for (int j = 0; j < points.length; ++j) {
                    if (used[j]) {
                        int d = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
                        if (d < dist) {
                            valid = false;
                            break;
                        }
                    }
                }
                if (valid) {
                    used[i] = true;
                    if (backtrack(points, k, dist, i + 1, used, count + 1)) return true;
                    used[i] = false;
                }
            }
        }
        return false;
    }
}
# @lc code=end