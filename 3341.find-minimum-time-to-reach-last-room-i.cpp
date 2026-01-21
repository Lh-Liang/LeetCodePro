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
        const long long INF = 1LL << 60;
        vector<vector<long long>> dist(n, vector<long long>(m, INF));
        dist[0][0] = 0;
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;
        pq.push({0, 0});
        int dx[4] = {-1, 0, 1, 0};
        int dy[4] = {0, 1, 0, -1};
        while (!pq.empty()) {
            auto [t, p] = pq.top(); pq.pop();
            int i = p / m;
            int j = p % m;
            if (t > dist[i][j]) continue;
            for (int d = 0; d < 4; ++d) {
                int ni = i + dx[d];
                int nj = j + dy[d];
                if (ni >= 0 && ni < n && nj >= 0 && nj < m) {
                    long long nt = max(t + 1, (long long)moveTime[ni][nj] + 1);
                    if (nt < dist[ni][nj]) {
                        dist[ni][nj] = nt;
                        pq.push({nt, ni * m + nj});
                    }
                }
            }
        }
        return dist[n - 1][m - 1];
    }
};
# @lc code=end