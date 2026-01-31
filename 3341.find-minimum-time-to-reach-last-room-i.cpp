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
        
        // Min-priority queue: {time, {row, col}}
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
            
            if (t > dist[r][c]) continue;
            if (r == n - 1 && c == m - 1) return t;
            
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                    // Arrival time at neighbor: max(current_time, opening_time) + 1 second travel
                    int next_t = max(t, moveTime[nr][nc]) + 1;
                    if (next_t < dist[nr][nc]) {
                        dist[nr][nc] = next_t;
                        pq.push({next_t, {nr, nc}});
                    }
                }
            }
        }
        
        return dist[n - 1][m - 1];
    }
};
# @lc code=end