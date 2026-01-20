#
# @lc app=leetcode id=3585 lang=cpp
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
    int n;
    vector<vector<pair<int, int>>> adj;
    vector<long long> dist;
    vector<int> depth;
    vector<vector<int>> up;
    int LOG;

    void dfs(int u, int p, int d, long long current_dist) {
        depth[u] = d;
        dist[u] = current_dist;
        up[u][0] = p;
        for (int i = 1; i < LOG; i++) {
            if (up[u][i - 1] != -1) {
                up[u][i] = up[up[u][i - 1]][i - 1];
            } else {
                up[u][i] = -1;
            }
        }
        for (auto& edge : adj[u]) {
            if (edge.first != p) {
                dfs(edge.first, u, d + 1, current_dist + edge.second);
            }
        }
    }

    int get_lca(int u, int v) {
        if (depth[u] < depth[v]) swap(u, v);
        for (int i = LOG - 1; i >= 0; i--) {
            if (up[u][i] != -1 && depth[up[u][i]] >= depth[v]) {
                u = up[u][i];
            }
        }
        if (u == v) return u;
        for (int i = LOG - 1; i >= 0; i--) {
            if (up[u][i] != up[v][i]) {
                u = up[u][i];
                v = up[v][i];
            }
        }
        return up[u][0];
    }

public:
    vector<int> findMedian(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        this->n = n;
        this->LOG = 18;
        adj.assign(n, vector<pair<int, int>>());
        for (auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }
        dist.assign(n, 0);
        depth.assign(n, 0);
        up.assign(n, vector<int>(LOG, -1));

        dfs(0, -1, 0, 0);

        vector<int> ans;
        for (auto& q : queries) {
            int u = q[0], v = q[1];
            int lca = get_lca(u, v);
            long long W = dist[u] + dist[v] - 2 * dist[lca];

            if (2 * (dist[u] - dist[lca]) >= W) {
                // Median is on the path u -> lca
                if (W == 0) {
                    ans.push_back(u);
                    continue;
                }
                int curr = u;
                // If u itself is the median
                if (2 * (dist[u] - dist[u]) >= W) {
                    ans.push_back(u);
                } else {
                    // Find the lowest ancestor x such that 2 * (dist[u] - dist[x]) >= W
                    for (int i = LOG - 1; i >= 0; i--) {
                        if (up[curr][i] != -1 && depth[up[curr][i]] >= depth[lca]) {
                            if (2 * (dist[u] - dist[up[curr][i]]) < W) {
                                curr = up[curr][i];
                            }
                        }
                    }
                    ans.push_back(up[curr][0]);
                }
            } else {
                // Median is on the path lca -> v
                // Condition: 2 * (dist[u] + dist[x] - 2 * dist[lca]) >= W
                long long target_val = W - 2 * dist[u] + 4 * dist[lca];
                int curr = v;
                // Find the highest ancestor x on path lca -> v such that 2 * dist[x] >= target_val
                for (int i = LOG - 1; i >= 0; i--) {
                    if (up[curr][i] != -1 && depth[up[curr][i]] >= depth[lca]) {
                        if (2 * dist[up[curr][i]] >= target_val) {
                            curr = up[curr][i];
                        }
                    }
                }
                ans.push_back(curr);
            }
        }
        return ans;
    }
};
# @lc code=end