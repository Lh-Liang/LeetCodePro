#
# @lc app=leetcode id=3341 lang=cpp
#
# [3341] Find Minimum Time to Reach Last Room I
#
# @lc code=start
#include <vector>
#include <queue>
using namespace std;
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = moveTime.size(), m = moveTime[0].size();
        vector<vector<int>> minTime(n, vector<int>(m, INT_MAX));
        priority_queue<pair<int, pair<int, int>>, vector<pair<int, pair<int, int>>>, greater<>> pq;
        minTime[0][0] = 0;
        pq.push({0, {0, 0}});
        int dirs[4][2] = {{1,0},{-1,0},{0,1},{0,-1}};
        while (!pq.empty()) {
            auto [curTime, pos] = pq.top(); pq.pop();
            int x = pos.first, y = pos.second;
            if (x == n-1 && y == m-1) return curTime;
            if (curTime > minTime[x][y]) continue;
            for (auto& d : dirs) {
                int nx = x + d[0], ny = y + d[1];
                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    int nextTime = max(curTime + 1, moveTime[nx][ny]);
                    if (nextTime < minTime[nx][ny]) {
                        minTime[nx][ny] = nextTime;
                        pq.push({nextTime, {nx, ny}});
                    }
                }
            }
        }
        return -1;
    }
};
# @lc code=end