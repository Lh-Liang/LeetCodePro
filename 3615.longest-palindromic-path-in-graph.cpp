#include <vector>
#include <string>
#include <queue>
#include <algorithm>

using namespace std;

#
# @lc app=leetcode id=3615 lang=cpp
#
# [3615] Longest Palindromic Path in Graph
#

# @lc code=start
class Solution {
public:
    struct State {
        int u, v, mask;
    };

    int maxLen(int n, vector<vector<int>>& edges, string label) {
        vector<int> adj[14];
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        vector<int> adj_by_label[14][26];
        for (int i = 0; i < n; ++i) {
            for (int neighbor : adj[i]) {
                adj_by_label[i][label[neighbor] - 'a'].push_back(neighbor);
            }
        }

        // visited[u][v][mask] where u <= v
        static bool visited[14][14][1 << 14];
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                for (int m = 0; m < (1 << n); ++m) {
                    visited[i][j][m] = false;
                }
            }
        }

        queue<State> q;
        int max_palindrome_len = 1;

        // Initial states: length 1
        for (int i = 0; i < n; ++i) {
            visited[i][i][1 << i] = true;
            q.push({i, i, 1 << i});
        }

        // Initial states: length 2
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            if (label[u] == label[v]) {
                int low = min(u, v);
                int high = max(u, v);
                int mask = (1 << u) | (1 << v);
                if (!visited[low][high][mask]) {
                    visited[low][high][mask] = true;
                    q.push({low, high, mask});
                    max_palindrome_len = max(max_palindrome_len, 2);
                }
            }
        }

        int current_len = 1;
        int nodes_at_current_len = q.size();

        while (!q.empty()) {
            State curr = q.front();
            q.pop();
            nodes_at_current_len--;

            int u = curr.u;
            int v = curr.v;
            int mask = curr.mask;

            // Calculate current length from mask popcount
            int len = 0;
            for (int i = 0; i < n; ++i) if (mask & (1 << i)) len++;
            max_palindrome_len = max(max_palindrome_len, len);

            for (int char_idx = 0; char_idx < 26; ++char_idx) {
                if (adj_by_label[u][char_idx].empty() || adj_by_label[v][char_idx].empty()) continue;
                for (int u_prime : adj_by_label[u][char_idx]) {
                    if (mask & (1 << u_prime)) continue;
                    for (int v_prime : adj_by_label[v][char_idx]) {
                        if (u_prime == v_prime || (mask & (1 << v_prime))) continue;

                        int next_u = min(u_prime, v_prime);
                        int next_v = max(u_prime, v_prime);
                        int next_mask = mask | (1 << u_prime) | (1 << v_prime);

                        if (!visited[next_u][next_v][next_mask]) {
                            visited[next_u][next_v][next_mask] = true;
                            q.push({next_u, next_v, next_mask});
                        }
                    }
                }
            }
        }

        return max_palindrome_len;
    }
};
# @lc code=end