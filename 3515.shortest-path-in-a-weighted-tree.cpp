#
# @lc app=leetcode id=3515 lang=cpp
#
# [3515] Shortest Path in a Weighted Tree
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <functional>

using namespace std;

class FenwickTree {
    int n;
    vector<long long> tree;
public:
    FenwickTree(int n) : n(n), tree(n + 2, 0) {}
    void add(int i, long long val) {
        for (; i <= n; i += i & -i) tree[i] += val;
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
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        vector<int> in(n + 1), out(n + 1), depth(n + 1);
        vector<int> parent_edge_weight(n + 1, 0);
        int timer = 0;
        
        function<void(int, int, int)> dfs = [&](int u, int p, int d) {
            in[u] = ++timer;
            depth[u] = d;
            for (auto& edge : adj[u]) {
                int v = edge.first;
                int w = edge.second;
                if (v != p) {
                    parent_edge_weight[v] = w;
                    dfs(v, u, d + 1);
                }
            }
            out[u] = timer;
        };
        dfs(1, 0, 0);

        FenwickTree ft(n);
        for (int i = 1; i <= n; ++i) {
            if (parent_edge_weight[i] != 0) {
                ft.add(in[i], parent_edge_weight[i]);
                ft.add(out[i] + 1, -(long long)parent_edge_weight[i]);
            }
        }

        vector<int> ans;
        for (const auto& q : queries) {
            if (q[0] == 1) {
                int u = q[1], v = q[2], next_w = q[3];
                int child = (depth[u] > depth[v]) ? u : v;
                int diff = next_w - parent_edge_weight[child];
                parent_edge_weight[child] = next_w;
                ft.add(in[child], diff);
                ft.add(out[child] + 1, -(long long)diff);
            } else {
                ans.push_back((int)ft.query(in[q[1]]));
            }
        }
        return ans;
    }
};
# @lc code=end