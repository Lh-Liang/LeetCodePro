#
# @lc app=leetcode id=3615 lang=cpp
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int maxLen(int n, vector<vector<int>>& edges, string label) {
        vector<vector<int>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }

        struct State {
            int u, v, mask, len;
        };

        // Visited array: visited[u][v][mask]
        // Flattened size: n * n * (1 << n)
        int mask_size = 1 << n;
        vector<bool> visited(n * n * mask_size, false);

        auto is_visited = [&](int u, int v, int mask) {
            return visited[(u * n + v) * mask_size + mask];
        };
        
        auto set_visited = [&](int u, int v, int mask) {
            visited[(u * n + v) * mask_size + mask] = true;
        };

        queue<State> q;
        int max_len = 1;

        // 1. Single nodes (Length 1)
        for (int i = 0; i < n; ++i) {
            int mask = 1 << i;
            // u=i, v=i
            if (!is_visited(i, i, mask)) {
                set_visited(i, i, mask);
                q.push({i, i, mask, 1});
            }
        }

        // 2. Edges with same label (Length 2)
        for (const auto& e : edges) {
            int u = e[0];
            int v = e[1];
            if (label[u] == label[v]) {
                if (u > v) swap(u, v);
                int mask = (1 << u) | (1 << v);
                if (!is_visited(u, v, mask)) {
                    set_visited(u, v, mask);
                    q.push({u, v, mask, 2});
                    max_len = max(max_len, 2);
                }
            }
        }

        while (!q.empty()) {
            State s = q.front();
            q.pop();

            int u = s.u;
            int v = s.v;
            int mask = s.mask;
            int len = s.len;

            // Try to expand from u to neighbor nu and v to neighbor nv
            for (int nu : adj[u]) {
                // nu must not be in current path
                if ((mask >> nu) & 1) continue;
                
                for (int nv : adj[v]) {
                    // nv must not be in current path and must be distinct from nu
                    if (nu == nv) continue;
                    if ((mask >> nv) & 1) continue;
                    
                    // Labels must match for palindrome property
                    if (label[nu] == label[nv]) {
                        int next_mask = mask | (1 << nu) | (1 << nv);
                        int next_u = nu;
                        int next_v = nv;
                        // Enforce canonical order u <= v to reduce states
                        if (next_u > next_v) swap(next_u, next_v);
                        
                        if (!is_visited(next_u, next_v, next_mask)) {
                            set_visited(next_u, next_v, next_mask);
                            int next_len = len + 2;
                            q.push({next_u, next_v, next_mask, next_len});
                            max_len = max(max_len, next_len);
                        }
                    }
                }
            }
        }

        return max_len;
    }
};
# @lc code=end