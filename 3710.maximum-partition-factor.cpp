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
#include <set>

using namespace std;

class Solution {
public:
    int maxPartitionFactor(vector<vector<int>>& points) {
        int n = points.size();
        if (n == 2) return 0;

        vector<int> distances;
        distances.reserve(n * (n - 1) / 2);
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                distances.push_back(abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]));
            }
        }
        sort(distances.begin(), distances.end());
        distances.erase(unique(distances.begin(), distances.end()), distances.end());

        auto isBipartite = [&](int threshold) {
            vector<vector<int>> adj(n);
            for (int i = 0; i < n; ++i) {
                for (int j = i + 1; j < n; ++j) {
                    if (abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1]) < threshold) {
                        adj[i].push_back(j);
                        adj[j].push_back(i);
                    }
                }
            }

            vector<int> color(n, -1);
            for (int i = 0; i < n; ++i) {
                if (color[i] == -1) {
                    queue<int> q;
                    q.push(i);
                    color[i] = 0;
                    while (!q.empty()) {
                        int u = q.front();
                        q.pop();
                        for (int v : adj[u]) {
                            if (color[v] == -1) {
                                color[v] = 1 - color[u];
                                q.push(v);
                            } else if (color[v] == color[u]) {
                                return false;
                            }
                        }
                    }
                }
            }
            return true;
        };

        int low = 0, high = distances.size() - 1, ans = 0;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (isBipartite(distances[mid])) {
                ans = distances[mid];
                low = mid + 1;
            } else {
                high = mid - 1;
            }
        }

        return ans;
    }
};
# @lc code=end