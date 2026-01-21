#
# @lc app=leetcode id=3435 lang=cpp
#
# [3435] Frequencies of Shortest Supersequences
#

# @lc code=start
#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> supersequences(vector<string>& words) {
        set<char> uniq;
        for (const auto& w : words) {
            uniq.insert(w[0]);
            uniq.insert(w[1]);
        }
        vector<char> lets(uniq.begin(), uniq.end());
        int m = lets.size();
        if (m == 0) return {};
        unordered_map<char, int> id_map;
        for (int i = 0; i < m; ++i) {
            id_map[lets[i]] = i;
        }
        vector<vector<bool>> adj(m, vector<bool>(m, false));
        vector<bool> has_self(m, false);
        for (const auto& w : words) {
            int u = id_map[w[0]];
            int v = id_map[w[1]];
            adj[u][v] = true;
            if (u == v) has_self[u] = true;
        }
        vector<int> cand;
        for (int i = 0; i < m; ++i) {
            if (!has_self[i]) cand.push_back(i);
        }
        int kk = cand.size();
        int max_safe = -1;
        vector<int> optimal_masks;
        for (int mask = 0; mask < (1 << kk); ++mask) {
            int ps = __builtin_popcount(mask);
            // build constraint graph
            vector<vector<int>> g(m);
            vector<int> indeg(m, 0);
            for (int j = 0; j < kk; ++j) {
                if (mask & (1 << j)) {
                    int v = cand[j];
                    for (int u = 0; u < m; ++u) {
                        if (adj[u][v]) {
                            g[u].push_back(v);
                            ++indeg[v];
                        }
                    }
                }
            }
            // Kahn's algorithm
            vector<int> temp_indeg = indeg;
            queue<int> q;
            for (int i = 0; i < m; ++i) {
                if (temp_indeg[i] == 0) q.push(i);
            }
            int cnt = 0;
            while (!q.empty()) {
                int u = q.front(); q.pop();
                ++cnt;
                for (int nei : g[u]) {
                    if (--temp_indeg[nei] == 0) {
                        q.push(nei);
                    }
                }
            }
            bool acyc = (cnt == m);
            if (acyc) {
                if (ps > max_safe) {
                    max_safe = ps;
                    optimal_masks = {mask};
                } else if (ps == max_safe) {
                    optimal_masks.push_back(mask);
                }
            }
        }
        set<vector<int>> freq_set;
        for (int mask : optimal_masks) {
            vector<bool> is_safe(m, false);
            for (int j = 0; j < kk; ++j) {
                if (mask & (1 << j)) {
                    is_safe[cand[j]] = true;
                }
            }
            vector<int> f(26, 0);
            for (int i = 0; i < m; ++i) {
                int cnt = is_safe[i] ? 1 : 2;
                f[lets[i] - 'a'] = cnt;
            }
            freq_set.insert(f);
        }
        return {freq_set.begin(), freq_set.end()};
    }
};
# @lc code=end