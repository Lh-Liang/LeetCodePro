#
# @lc app=leetcode id=3341 lang=cpp
#
# [3341] Find Minimum Time to Reach Last Room I
#

# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size();
        int m = moveTime[0].size();
        
        // dist[i][j] stores the minimum time to reach room (i, j)
        // Initialize with a large value (INT_MAX)
        vector<vector<int>> dist(n, vector<int>(m, 2147483647));
        dist[0][0] = 0;
        
        // Min-heap: {time, {row, col}}
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        pq.push({0, {0, 0}});
        
        int dr[] = {0, 0, 1, -1};
        int dc[] = {1, -1, 0, 0};
        
        while (!pq.empty()) {
            int d = pq.top().first;
            int r = pq.top().second.first;
            int c = pq.top().second.second;
            pq.pop();
            
            // If we found a better path already, skip this one
            if (d > dist[r][c]) continue;
            
            // If we reached the target, return the time
            if (r == n - 1 && c == m - 1) return d;
            
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                    // Transition: time to enter is max(current_time, room_open_time) + move_cost
                    int next_d = max(d, moveTime[nr][nc]) + 1;
                    if (next_d < dist[nr][nc]) {
                        dist[nr][nc] = next_d;
                        pq.push({next_d, {nr, nc}});
                    }
                }
            }
        }
        
        return dist[n - 1][m - 1];
    }
};
# @lc code=end