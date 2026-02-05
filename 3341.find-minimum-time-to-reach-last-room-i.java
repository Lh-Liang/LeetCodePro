#
# @lc app=leetcode id=3341 lang=java
#
# [3341] Find Minimum Time to Reach Last Room I
#
# @lc code=start
import java.util.*;
class Solution {
    public int minTimeToReach(int[][] moveTime) {
        int n = moveTime.length, m = moveTime[0].length;
        int[][] minTime = new int[n][m];
        for (int[] row : minTime) Arrays.fill(row, Integer.MAX_VALUE);
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, 0, 0}); // {currentTime, x, y}
        minTime[0][0] = 0;
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, 1, -1};
        while (!pq.isEmpty()) {
            int[] cur = pq.poll();
            int t = cur[0], x = cur[1], y = cur[2];
            if (x == n - 1 && y == m - 1) return t;
            for (int d = 0; d < 4; d++) {
                int nx = x + dx[d], ny = y + dy[d];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    int arrive = Math.max(t + 1, moveTime[nx][ny]);
                    if (arrive < minTime[nx][ny]) { // Only proceed if strictly better
                        minTime[nx][ny] = arrive;
                        pq.offer(new int[]{arrive, nx, ny});
                    }
                }
            }
        }
        return -1; // Should not reach here given constraints
    }
}
# @lc code=end