#
# @lc app=leetcode id=3341 lang=java
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
import java.util.PriorityQueue;
import java.util.Comparator;

class Solution {
    public int minTimeToReach(int[][] moveTime) {
        int n = moveTime.length;
        int m = moveTime[0].length;
        boolean[][] visited = new boolean[n][m];
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[2])); // [row, col, time]
        pq.offer(new int[]{0, 0, 0}); // start at (0, 0) at t = 0

        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}}; // down, up, right, left
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int row = current[0], col = current[1], time = current[2];
            if (row == n - 1 && col == m - 1) return time; // reached target
            if (visited[row][col]) continue; // already visited this cell
            visited[row][col] = true;
            for (int[] dir : directions) {
                int newRow = row + dir[0], newCol = col + dir[1];
                if (newRow >= 0 && newRow < n && newCol >= 0 && newCol < m && !visited[newRow][newCol]) {
                    int nextTime = Math.max(time + 1, moveTime[newRow][newCol]); // wait if needed until room opens
                    pq.offer(new int[]{newRow, newCol, nextTime});
                }
            }
        }
        return -1; // should never reach here since we know it's always possible to reach (n-1,m-1) based on constraints. 
    } 
}
# @lc code=end