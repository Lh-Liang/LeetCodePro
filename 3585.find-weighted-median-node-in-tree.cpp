#
# @lc app=leetcode id=3585 lang=cpp
#
# [3585] Find Weighted Median Node in Tree
#

# @lc code=start
class Solution {
public:
    static const int LOG = 20;
    vector<vector<pair<int, int>>> adj;
    vector<vector<int>> up; // up[v][k] = 2^k ancestor of v
    vector<int> depth;
    vector<long long> preSum; // prefix sum of edge weights from root

    void dfs(int v, int p, int d, long long sum) {
        up[v][0] = p;
        depth[v] = d;
        preSum[v] = sum;
        for (auto &[to, w] : adj[v]) {
            if (to != p) dfs(to, v, d + 1, sum + w);
        }
    }

    int lca(int u, int v) {
        if (depth[u] < depth[v]) std::swap(u, v);
        for (int k = LOG - 1; k >= 0; --k) {
            if (depth[u] - (1 << k) >= depth[v]) u = up[u][k];
        }
        if (u == v) return u;
        for (int k = LOG - 1; k >= 0; --k) {
            if (up[u][k] != up[v][k]) {
                u = up[u][k];
                v = up[v][k];
            }
        }
        return up[u][0];
    }

    int go_up(int u, int steps) {
        for (int k = 0; k < LOG; ++k) {
            if (steps & (1 << k)) u = up[u][k];
        }
        return u;
    }

    vector<int> findMedian(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        adj.assign(n, {});
        for (auto &e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].emplace_back(v, w);
            adj[v].emplace_back(u, w);
        }
        up.assign(n, vector<int>(LOG));
        depth.assign(n, 0);
        preSum.assign(n, 0);
        dfs(0, 0, 0, 0);
        for (int k = 1; k < LOG; ++k) {
            for (int v = 0; v < n; ++v) {
                up[v][k] = up[up[v][k - 1]][k - 1];
            }
        }
        vector<int> ans;
        for (auto &q : queries) {
            int u = q[0], v = q[1];
            int anc = lca(u, v);
            long long total = preSum[u] + preSum[v] - 2 * preSum[anc];
            long long half = (total + 1) / 2; // strictly at least half
            // Go from u towards v
            int cur = u;
            long long sum = 0;
            if (u == v) {
                ans.push_back(u);
                continue;
            }
            // First, try to go up from u to anc
            for (int k = LOG - 1; k >= 0; --k) {
                if (depth[cur] - (1 << k) >= depth[anc]) {
                    int nxt = up[cur][k];
                    long long seg = preSum[cur] - preSum[nxt];
                    if (sum + seg >= half) {
                        // need to binary search down this segment
                        int low = cur, high = nxt, res = cur;
                        while (low != high) {
                            int mid = go_up(low, depth[low] - depth[high] - 1);
                            if (sum + preSum[cur] - preSum[mid] >= half) low = mid;
                            else { res = mid; high = mid; }
                        }
                        ans.push_back(low);
                        goto next_query;
                    } else {
                        sum += seg;
                        cur = nxt;
                    }
                }
            }
            // Now go down from anc to v
            vector<int> path;
            int x = v;
            while (x != anc) { path.push_back(x); x = up[x][0]; }
            reverse(path.begin(), path.end());
            for (int node : path) {
                long long seg = preSum[node] - preSum[up[node][0]];
                if (sum + seg >= half) {
                    ans.push_back(node);
                    goto next_query;
                } else {
                    sum += seg;
                }
            }
            ans.push_back(v);
        next_query:;
        }
        return ans;
    }
};
# @lc code=end