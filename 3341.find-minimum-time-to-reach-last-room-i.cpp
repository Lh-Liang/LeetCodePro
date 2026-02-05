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
        int n = moveTime.size(), m = moveTime[0].size();
        vector<vector<int>> minTime(n, vector<int>(m, INT_MAX));
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<tuple<int, int, int>>> pq;
        pq.push({0, 0, 0}); // time, x, y
        minTime[0][0] = 0;
        vector<pair<int, int>> dirs = {{0,1},{1,0},{0,-1},{-1,0}};
        while (!pq.empty()) {
            auto [t, x, y] = pq.top(); pq.pop();
            if (x == n-1 && y == m-1) return t;
            if (t > minTime[x][y]) continue;
            for (auto& d : dirs) {
                int nx = x + d.first, ny = y + d.second;
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    int arrive = max(t + 1, moveTime[nx][ny]);
                    if (arrive < minTime[nx][ny]) {
                        minTime[nx][ny] = arrive;
                        pq.push({arrive, nx, ny});
                    }
                }
            }
        }
        return -1;
    }
};
# @lc code=end