#
# @lc app=leetcode id=3341 lang=cpp
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size();
        int m = moveTime[0].size();
        
        // dist[i][j] stores the minimum time to reach room (i, j)
        vector<vector<int>> dist(n, vector<int>(m, INT_MAX));
        
        // Min-priority queue for Dijkstra's algorithm: {time, {row, col}}
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        
        // Starting at (0, 0) at time t = 0
        dist[0][0] = 0;
        pq.push({0, {0, 0}});
        
        // Directions for movement: right, left, down, up
        int dr[] = {0, 0, 1, -1};
        int dc[] = {1, -1, 0, 0};
        
        while (!pq.empty()) {
            int d = pq.top().first;
            int r = pq.top().second.first;
            int c = pq.top().second.second;
            pq.pop();
            
            // If we have already found a shorter path to (r, c), skip it
            if (d > dist[r][c]) continue;
            
            // If we reached the target room, we can return the time immediately
            if (r == n - 1 && c == m - 1) return d;
            
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                // Check if the neighbor is within grid boundaries
                if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                    // Arrival time at neighbor is max(current_time, moveTime[nr][nc]) + 1
                    int next_dist = max(d, moveTime[nr][nc]) + 1;
                    
                    if (next_dist < dist[nr][nc]) {
                        dist[nr][nc] = next_dist;
                        pq.push({next_dist, {nr, nc}});
                    }
                }
            }
        }
        
        return dist[n - 1][m - 1];
    }
};
# @lc code=end