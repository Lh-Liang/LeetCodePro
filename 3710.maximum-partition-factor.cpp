#
# @lc app=leetcode id=3710 lang=cpp
#
# [3710] Maximum Partition Factor
#

# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maxPartitionFactor(vector<vector<int>>& points) {
        int n = points.size();
        if (n == 2) return 0;
        // Step 1: Get all unique pairwise manhattan distances
        vector<int> dists;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                int d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                dists.push_back(d);
            }
        }
        sort(dists.begin(), dists.end());
        dists.erase(unique(dists.begin(), dists.end()), dists.end());

        // Helper: check if for partition factor >= d, the graph is bipartite and both groups are non-empty
        auto isValidPartition = [&](int d) -> bool {
            vector<vector<int>> g(n);
            for (int i = 0; i < n; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    int dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]);
                    if (dist < d) {
                        g[i].push_back(j);
                        g[j].push_back(i);
                    }
                }
            }
            vector<int> color(n, -1);
            int count[2] = {0, 0};
            for (int i = 0; i < n; ++i) {
                if (color[i] == -1) {
                    queue<int> q;
                    q.push(i);
                    color[i] = 0;
                    count[0]++;
                    while (!q.empty()) {
                        int u = q.front(); q.pop();
                        for (int v : g[u]) {
                            if (color[v] == -1) {
                                color[v] = color[u] ^ 1;
                                count[color[v]]++;
                                q.push(v);
                            } else if (color[v] == color[u]) {
                                return false;
                            }
                        }
                    }
                }
            }
            // Explicitly check both groups are non-empty
            if (count[0] == 0 || count[1] == 0) return false;
            return true;
        };
        // Binary search
        int l = 0, r = dists.size() - 1, ans = 0;
        while (l <= r) {
            int m = (l + r) / 2;
            int d = dists[m];
            if (isValidPartition(d)) {
                ans = d;
                l = m + 1;
            } else {
                r = m - 1;
            }
        }
        return ans;
    }
};
# @lc code=end