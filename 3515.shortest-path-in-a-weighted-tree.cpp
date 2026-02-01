#
# @lc app=leetcode id=3515 lang=cpp
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
#include <vector>
#include <utility>
#include <stack>

using namespace std;

class FenwickTree {
    int n;
    vector<long long> tree;
public:
    FenwickTree(int n) : n(n), tree(n + 1, 0) {}
    void update(int i, long long delta) {
        if (i <= 0 || i > n) return;
        for (; i <= n; i += i & -i) tree[i] += delta;
    }
    long long query(int i) {
        long long sum = 0;
        for (; i > 0; i -= i & -i) sum += tree[i];
        return sum;
    }
};

class Solution {
public:
    vector<int> treeQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        vector<vector<pair<int, int>>> adj(n + 1);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back({edge[1], edge[2]});
            adj[edge[1]].push_back({edge[0], edge[2]});
        }

        vector<int> in(n + 1), out(n + 1), depth(n + 1), edge_weight_to_parent(n + 1, 0);
        int timer = 0;

        // Iterative DFS to avoid stack overflow
        struct Frame {
            int u, p, d, neighbor_idx;
        };
        stack<Frame> st;
        st.push({1, 0, 0, 0});
        in[1] = ++timer;

        while (!st.empty()) {
            Frame& top = st.top();
            int u = top.u, p = top.p, d = top.d;

            if (top.neighbor_idx < adj[u].size()) {
                auto [v, w] = adj[u][top.neighbor_idx];
                top.neighbor_idx++;
                if (v != p) {
                    in[v] = ++timer;
                    depth[v] = d + 1;
                    edge_weight_to_parent[v] = w;
                    st.push({v, u, d + 1, 0});
                }
            } else {
                out[u] = timer;
                st.pop();
            }
        }

        FenwickTree bit(n);
        // Initial distances using difference array logic in Fenwick Tree
        for (int i = 1; i <= n; ++i) {
            if (edge_weight_to_parent[i] != 0) {
                bit.update(in[i], edge_weight_to_parent[i]);
                bit.update(out[i] + 1, -edge_weight_to_parent[i]);
            }
        }

        vector<int> results;
        for (const auto& q : queries) {
            if (q[0] == 1) {
                int u = q[1], v = q[2], w_new = q[3];
                int child = (depth[u] > depth[v]) ? u : v;
                int delta = w_new - edge_weight_to_parent[child];
                bit.update(in[child], delta);
                bit.update(out[child] + 1, -delta);
                edge_weight_to_parent[child] = w_new;
            } else {
                results.push_back((int)bit.query(in[q[1]]));
            }
        }

        return results;
    }
};
# @lc code=end