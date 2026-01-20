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
        
        // dist[i][j] will store the minimum time to reach cell (i, j)
        vector<vector<int>> dist(n, vector<int>(m, 2e9 + 7));
        dist[0][0] = 0;
        
        // Min-priority queue: {time, row, col}
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<pair<int, pair<int, int>>>> pq;
        pq.push({0, {0, 0}});
        
        int dr[] = {0, 0, 1, -1};
        int dc[] = {1, -1, 0, 0};
        
        while (!pq.empty()) {
            int d = pq.top().first;
            int r = pq.top().second.first;
            int c = pq.top().second.second;
            pq.pop();
            
            if (d > dist[r][c]) continue;
            if (r == n - 1 && c == m - 1) return d;
            
            for (int i = 0; i < 4; ++i) {
                int nr = r + dr[i];
                int nc = c + dc[i];
                
                if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                    // Time to reach neighbor: wait until moveTime[nr][nc] if necessary, then 1 sec to move
                    int nextTime = max(d, moveTime[nr][nc]) + 1;
                    if (nextTime < dist[nr][nc]) {
                        dist[nr][nc] = nextTime;
                        pq.push({nextTime, {nr, nc}});
                    }
                }
            }
        }
        
        return dist[n - 1][m - 1];
    }
};
# @lc code=end