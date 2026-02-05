#
# @lc app=leetcode id=3538 lang=java
#
# [3538] Merge Operations for Minimum Travel Time
#
# @lc code=start
import java.util.PriorityQueue;
import java.util.Comparator;

class Solution {
    public int minTravelTime(int l, int n, int k, int[] position, int[] time) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Comparator.comparingInt(i -> time[i] + time[i + 1]));
        for (int i = 1; i < n - 1; i++) {
            pq.offer(i);
        }
        
        while (k-- > 0 && !pq.isEmpty()) {
            int index = pq.poll();
            // Merge operation
            if (index < n - 1) {
                time[index + 1] += time[index];
                // Shift positions and times leftwards to remove index
                System.arraycopy(position, index + 1, position, index, n - index - 1);
                System.arraycopy(time, index + 1, time, index, n - index - 1);
                n--;
                // Update priority queue with affected indices
                if (index > 0) pq.offer(index - 1);
                if (index < n - 1) pq.offer(index);
            }
        }
        
        // Calculate total travel time after all merges
        int totalTravelTime = 0;
        for (int i = 0; i < n - 1; i++) {
            totalTravelTime += (position[i + 1] - position[i]) * time[i];
        }
        return totalTravelTime;
    }
}
# @lc code=end