#
# @lc app=leetcode id=3710 lang=cpp
#
# [3710] Maximum Partition Factor
#
# @lc code=start
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

class Solution {
public:
    int maxPartitionFactor(vector<vector<int>>& points) {
        int n = points.size();
        if (n == 2) return 0;

        vector<long long> distances;
        distances.push_back(0);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                distances.push_back(abs((long long)points[i][0] - points[j][0]) + abs((long long)points[i][1] - points[j][1]));
            }
        }
        sort(distances.begin(), distances.end());
        distances.erase(unique(distances.begin(), distances.end()), distances.end());

        auto is_bipartite = [&](long long limit) {
            if (limit == 0) return true;
            vector<int> color(n, 0); // 0: uncolored, 1: group1, 2: group2
            for (int i = 0; i < n; ++i) {
                if (color[i] == 0) {
                    queue<int> q;
                    q.push(i);
                    color[i] = 1;
                    while (!q.empty()) {
                        int u = q.front();
                        q.pop();
                        for (int v = 0; v < n; ++v) {
                            if (u == v) continue;
                            long long d = abs((long long)points[u][0] - points[v][0]) + abs((long long)points[u][1] - points[v][1]);
                            if (d < limit) {
                                if (color[v] == 0) {
                                    color[v] = 3 - color[u];
                                    q.push(v);
                                } else if (color[v] == color[u]) {
                                    return false;
                                }
                            }
                        }
                    }
                }
            }
            return true;
        };

        int low = 0, high = distances.size() - 1;
        long long ans = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (is_bipartite(distances[mid])) {
                ans = distances[mid];
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return (int)ans;
    }
};
# @lc code=end