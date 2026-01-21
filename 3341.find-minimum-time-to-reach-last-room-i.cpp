#
# @lc app=leetcode id=3341 lang=cpp
#
# [3341] Find Minimum Time to Reach Last Room I
#
# @lc code=start
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size();
        int m = moveTime[0].size();
        
        // Priority queue: (time, row, col)
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
        
        // Distance array to track minimum time to reach each cell
        vector<vector<int>> dist(n, vector<int>(m, INT_MAX));
        
        // Start at (0, 0) at time 0
        pq.push({0, 0, 0});
        dist[0][0] = 0;
        
        // Directions: up, down, left, right
        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};
        
        while (!pq.empty()) {
            auto [time, x, y] = pq.top();
            pq.pop();
            
            // If we've reached the destination
            if (x == n - 1 && y == m - 1) {
                return time;
            }
            
            // Skip if we've already found a better path to this cell
            if (time > dist[x][y]) {
                continue;
            }
            
            // Try all 4 directions
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                // Check bounds
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    // Calculate arrival time at (nx, ny)
                    int arrivalTime = max(time, moveTime[nx][ny]) + 1;
                    
                    // If this is a better path, update and add to queue
                    if (arrivalTime < dist[nx][ny]) {
                        dist[nx][ny] = arrivalTime;
                        pq.push({arrivalTime, nx, ny});
                    }
                }
            }
        }
        
        return dist[n - 1][m - 1];
    }
};
# @lc code=end