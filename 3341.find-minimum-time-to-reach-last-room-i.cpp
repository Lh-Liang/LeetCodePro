# 
# @lc app=leetcode id=3341 lang=cpp
# 
# [3341] Find Minimum Time to Reach Last Room I
# 
# @lc code=start
#include <vector>
#include <queue>
#include <tuple>
using namespace std;
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size();
        int m = moveTime[0].size();
        vector<vector<int>> minTime(n, vector<int>(m, INT_MAX));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        pq.push({0, 0, 0}); // {time, row, col}
        minTime[0][0] = 0;
        vector<int> dir = {-1, 0, 1, 0, -1}; // Directions for moving in grid
        while (!pq.empty()) {
            auto [t, r, c] = pq.top(); pq.pop();
            if (r == n - 1 && c == m - 1) return t; // Reached last room
            for (int i = 0; i < 4; ++i) { // Explore all directions
                int nr = r + dir[i], nc = c + dir[i + 1];
                if (nr >= 0 && nr < n && nc >= 0 && nc < m) {
                    int waitTime = max(t + 1, moveTime[nr][nc]); // Wait if needed before moving
                    if (waitTime < minTime[nr][nc]) {
                        minTime[nr][nc] = waitTime;
                        pq.push({waitTime, nr, nc});
                    }
                }
            }
        }
        return -1; // Should never reach here if input is valid as per constraint. 
    }
};
# @lc code=end