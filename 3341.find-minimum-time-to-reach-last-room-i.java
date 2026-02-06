#
# @lc app=leetcode id=3341 lang=java
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
import java.util.PriorityQueue;
import java.util.Arrays;

class Solution {
    public int minTimeToReach(int[][] moveTime) {
        int n = moveTime.length;
        int m = moveTime[0].length;
        int[][] minTime = new int[n][m];
        for (int[] row : minTime) { Arrays.fill(row, Integer.MAX_VALUE); }
        minTime[0][0] = 0;
        PriorityQueue<int[]> pq = new PriorityQueue<>((a, b) -> a[2] - b[2]); // [x, y, current_time]
        pq.offer(new int[]{0, 0, 0});
        int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int x = current[0], y = current[1], time = current[2];
            if (x == n - 1 && y == m - 1) return time; // Reached end room.
            for (int[] dir : directions) {
                int nx = x + dir[0], ny = y + dir[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) { // Check boundaries.
                    int waitTime = Math.max(0, moveTime[nx][ny] - (time + 1)); // Wait if needed. 
                    int newTime = time + 1 + waitTime; 
                    if (newTime < minTime[nx][ny]) { 
                        minTime[nx][ny] = newTime; 
                        pq.offer(new int[]{nx, ny, newTime}); 
                    } 
                } 
            } 
        } 
d return -1; // Should never reach here if input is valid. 
l } 
l} 
l# @lc code=end