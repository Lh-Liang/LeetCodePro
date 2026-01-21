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
        
        // Min heap: (time, row, col)
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
        
        // Distance array to track minimum time to reach each cell
        vector<vector<int>> dist(n, vector<int>(m, INT_MAX));
        
        pq.push({0, 0, 0});
        dist[0][0] = 0;
        
        int dx[] = {-1, 1, 0, 0};
        int dy[] = {0, 0, -1, 1};
        
        while (!pq.empty()) {
            auto [time, x, y] = pq.top();
            pq.pop();
            
            if (x == n - 1 && y == m - 1) {
                return time;
            }
            
            if (time > dist[x][y]) {
                continue;
            }
            
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    int newTime = max(time, moveTime[nx][ny]) + 1;
                    
                    if (newTime < dist[nx][ny]) {
                        dist[nx][ny] = newTime;
                        pq.push({newTime, nx, ny});
                    }
                }
            }
        }
        
        return dist[n-1][m-1];
    }
};
# @lc code=end