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
        // Distance matrix initialized with large values
        vector<vector<long long>> dist(n, vector<long long>(m, LLONG_MAX));
        // Min-heap priority queue storing {time, row, col}
        using Node = pair<long long, pair<int,int>>;
        priority_queue<Node, vector<Node>, greater<Node>> pq;
        
        // Start at top-left corner
        dist[0][0] = moveTime[0][0];
        pq.push({dist[0][0], {0, 0}});
        
        // Directions: up down left right
        int dirs[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        
        while (!pq.empty()) {
            auto cur = pq.top();
            pq.pop();
            long long cur_time = cur.first;
            int r = cur.second.first;
            int c = cur.second.second;
            
            // Skip outdated entries
            if (cur_time > dist[r][c]) continue;
            
            // Explore neighbors
            for (auto& dir : dirs) {
                int nr = r + dir[0];
                int nc = c + dir[1];
                
                // Check bounds
                if (nr < 0 || nr >= n || nc < 0 || nc >= m)
                    continue;
                
                // New arrival time
                long long new_time = max(cur_time + 1LL,
                                         static_cast<long long>(moveTime[nr][nc]));
                
                // Relaxation step
                if (new_time < dist[nr][nc]) {
                    dist[nr][nc] = new_time;
                    pq.push({new_time, {nr, nc}});
                }
            }
        }
        
        return static_cast<int>(dist[n-1][m-1]);
    }
};
# @lc code=end