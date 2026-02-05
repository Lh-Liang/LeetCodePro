#
# @lc app=leetcode id=3464 lang=java
#
# [3464] Maximize the Distance Between Points on a Square
#
# @lc code=start
class Solution {
    public int maxDistance(int side, int[][] points, int k) {
        int n = points.length;
        int[][] dist = new int[n][n];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                dist[i][j] = Math.abs(points[i][0] - points[j][0]) + Math.abs(points[i][1] - points[j][1]);
            }
        }
        int left = 0, right = 2 * side, ans = 0;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (canPick(points, dist, k, mid)) {
                ans = mid;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return ans;
    }
    private boolean canPick(int[][] points, int[][] dist, int k, int d) {
        int n = points.length;
        return dfs(points, dist, k, d, new boolean[n], 0, 0);
    }
    private boolean dfs(int[][] points, int[][] dist, int k, int d, boolean[] used, int start, int cnt) {
        if (cnt == k) {
            int n = points.length;
            for (int i = 0; i < n; ++i) {
                if (!used[i]) continue;
                for (int j = i + 1; j < n; ++j) {
                    if (used[j] && dist[i][j] < d) return false;
                }
            }
            return true;
        }
        int n = points.length;
        for (int i = start; i < n; ++i) {
            boolean valid = true;
            for (int j = 0; j < n; ++j) {
                if (used[j] && dist[i][j] < d) { valid = false; break; }
            }
            if (valid) {
                used[i] = true;
                if (dfs(points, dist, k, d, used, i + 1, cnt + 1)) return true;
                used[i] = false;
            }
        }
        return false;
    }
}
# @lc code=end