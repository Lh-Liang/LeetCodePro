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
        for (int[] row : minTime)
            Arrays.fill(row, Integer.MAX_VALUE);
        minTime[0][0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.offer(new int[]{0, 0, 0}); // {time, i, j}
        int[] dirs = {0, 1, 0, -1, 0};
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int time = curr[0], i = curr[1], j = curr[2];
            if (i == n-1 && j == m-1) return time;
            if (time > minTime[i][j]) continue;
            for (int d = 0; d < 4; ++d) {
                int ni = i + dirs[d], nj = j + dirs[d+1];
                if (ni >= 0 && ni < n && nj >= 0 && nj < m) {
                    int nextTime = Math.max(time + 1, moveTime[ni][nj]);
                    if (nextTime < minTime[ni][nj]) {
                        minTime[ni][nj] = nextTime;
                        pq.offer(new int[]{nextTime, ni, nj});
                    }
                }
            }
        }
        return -1;
    }
}
# @lc code=end