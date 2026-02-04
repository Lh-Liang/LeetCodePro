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
        vector<vector<int>> minTime(n, vector<int>(m, INT_MAX)); // Initialize min times as infinity
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        pq.emplace(0, 0, 0); // Start at (0, 0) with time=0
        minTime[0][0] = 0;
        vector<pair<int,int>> directions = {{1,0}, {-1,0}, {0,1}, {0,-1}}; // Possible moves: down, up, right, left
        while (!pq.empty()) {
            auto [current_time, x, y] = pq.top(); pq.pop();
            if (x == n - 1 && y == m - 1) return current_time; // Reached destination
            for (auto [dx, dy] : directions) {
                int nx = x + dx; 
                int ny = y + dy; 
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) { // Check bounds
                    int next_time = max(current_time + 1, moveTime[nx][ny]); // Calculate next possible time
                    if (next_time < minTime[nx][ny]) { // Check if this is a better option
                        minTime[nx][ny] = next_time;
                        pq.emplace(next_time, nx, ny);
                    }
                }
            }
        } 
        return -1; // Unreachable code due to constraints ensuring a path exists. 
    } 
}; 
# @lc code=end