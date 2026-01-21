#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3341 lang=cpp
 *
 * [3341] Find Minimum Time to Reach Last Room I
 */

// @lc code=start
class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int n = (int)moveTime.size();
        int m = (int)moveTime[0].size();

        const long long INF = (1LL << 62);
        vector<vector<long long>> dist(n, vector<long long>(m, INF));

        using State = pair<long long, pair<int,int>>; // (time, (x,y))
        priority_queue<State, vector<State>, greater<State>> pq;

        dist[0][0] = 0;
        pq.push({0, {0, 0}});

        int dx[4] = {1, -1, 0, 0};
        int dy[4] = {0, 0, 1, -1};

        while (!pq.empty()) {
            auto [t, pos] = pq.top();
            pq.pop();
            int x = pos.first, y = pos.second;

            if (t != dist[x][y]) continue;
            if (x == n - 1 && y == m - 1) return (int)t;

            for (int k = 0; k < 4; k++) {
                int nx = x + dx[k], ny = y + dy[k];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) continue;

                long long nt = max(t, (long long)moveTime[nx][ny]) + 1;
                if (nt < dist[nx][ny]) {
                    dist[nx][ny] = nt;
                    pq.push({nt, {nx, ny}});
                }
            }
        }

        return (int)dist[n - 1][m - 1];
    }
};
// @lc code=end
