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
        // Using a large value for initialization (2e9 + 7 stays within int range)
        vector<vector<int>> dist(n, vector<int>(m, 2000000000));
        // Priority queue stores {time, {row, col}}, ordered by time (min-priority queue)
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        
        dist[0][0] = 0;
        pq.push({0, {0, 0}});
        
        int dr[] = {0, 0, 1, -1};
        int dc[] = {1, -1, 0, 0};
        
        while (!pq.empty()) {
            auto [t, pos] = pq.top();
            pq.pop();
            
            int r = pos.first;
            int c = pos.second;
            
            // If we found a better way already, skip this
            if (t > dist[r][c]) continue;
            
            // If we reached the destination
            if (r == n - 1 && c == m - 1) return t;
            
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                    // Time to reach neighbor: max(current time, opening time) + 1 second travel
                    int nt = max(t, moveTime[nr][nc]) + 1;
                    if (nt < dist[nr][nc]) {
                        dist[nr][nc] = nt;
                        pq.push({nt, {nr, nc}});
                    }
                }
            }
        }
        
        return dist[n - 1][m - 1];
    }
};
# @lc code=end