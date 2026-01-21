#include <bits/stdc++.h>
using namespace std;

/*
 * @lc app=leetcode id=3786 lang=cpp
 *
 * [3786] Total Sum of Interaction Cost in Tree Groups
 */

// @lc code=start
class Solution {
public:
    long long interactionCosts(int n, vector<vector<int>>& edges, vector<int>& group) {
        static const int G = 20;
        vector<vector<int>> adj(n);
        adj.reserve(n);
        for (auto &e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }

        array<int, G + 1> total{};
        total.fill(0);
        for (int i = 0; i < n; i++) total[group[i]]++;

        // Build parent and traversal order (root at 0)
        vector<int> parent(n, -1), order;
        order.reserve(n);
        stack<int> st;
        parent[0] = 0;
        st.push(0);
        while (!st.empty()) {
            int u = st.top();
            st.pop();
            order.push_back(u);
            for (int v : adj[u]) {
                if (v == parent[u]) continue;
                parent[v] = u;
                st.push(v);
            }
        }

        vector<array<int, G + 1>> sub(n);
        long long ans = 0;

        // Postorder accumulation
        for (int i = (int)order.size() - 1; i >= 0; --i) {
            int u = order[i];
            sub[u].fill(0);
            sub[u][group[u]] = 1;

            for (int v : adj[u]) {
                if (parent[v] != u) continue; // v is a child of u

                // edge (u-v) contribution for each group
                for (int g = 1; g <= G; g++) {
                    long long cnt = sub[v][g];
                    if (cnt) ans += cnt * ( (long long)total[g] - cnt );
                    sub[u][g] += sub[v][g];
                }
            }
        }

        return ans;
    }
};
// @lc code=end
