#
# @lc app=leetcode id=3341 lang=cpp
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size();
        int m = moveTime[0].size();
        
        // dist[r][c] stores the minimum time to reach room (r, c)
        vector<vector<int>> dist(n, vector<int>(m, INT_MAX));
        
        // Priority queue stores {time, {row, col}}, ordered by time ascending (min-heap)
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        
        dist[0][0] = 0;
        pq.push({0, {0, 0}});
        
        int dr[] = {0, 0, 1, -1};
        int dc[] = {1, -1, 0, 0};
        
        while (!pq.empty()) {
            int t = pq.top().first;
            int r = pq.top().second.first;
            int c = pq.top().second.second;
            pq.pop();
            
            // Standard Dijkstra optimization: skip if a better path was already processed
            if (t > dist[r][c]) continue;
            
            // Early exit if we reached the target
            if (r == n - 1 && c == m - 1) return t;
            
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                    // Arrival time is max of (current time, opening time) + 1 second travel
                    int arrival = max(t, moveTime[nr][nc]) + 1;
                    
                    if (arrival < dist[nr][nc]) {
                        dist[nr][nc] = arrival;
                        pq.push({arrival, {nr, nc}});
                    }
                }
            }
        }
        
        return dist[n - 1][m - 1];
    }
};
# @lc code=end