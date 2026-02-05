#
# @lc app=leetcode id=3710 lang=cpp
#
# [3710] Maximum Partition Factor
#

# @lc code=start
class Solution {
public:
    int maxPartitionFactor(vector<vector<int>>& points) {
        int n = points.size();
        if (n == 2) return 0;

        // Helper to check if graph (edges with dist < d) is bipartite
        auto is_bipartite = [&](int d) {
            vector<vector<int>> g(n);
            for (int i = 0; i < n; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    int manhattan = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                    if (manhattan < d) {
                        g[i].push_back(j);
                        g[j].push_back(i);
                    }
                }
            }
            vector<int> color(n, -1);
            for (int i = 0; i < n; ++i) {
                if (color[i] != -1) continue;
                queue<int> q;
                q.push(i);
                color[i] = 0;
                while (!q.empty()) {
                    int u = q.front(); q.pop();
                    for (int v : g[u]) {
                        if (color[v] == -1) {
                            color[v] = color[u] ^ 1;
                            q.push(v);
                        } else if (color[v] == color[u]) {
                            return false;
                        }
                    }
                }
            }
            return true;
        };

        // Set search bounds. Manhattan distances range up to 4e8
        int l = 1, r = 400000001, ans = 0;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (is_bipartite(m)) {
                ans = m;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return ans;
    }
};
# @lc code=end