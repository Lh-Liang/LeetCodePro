#
# @lc app=leetcode id=3786 lang=cpp
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#
# @lc code=start
class Solution {
public:
    long long interactionCosts(int n, vector<vector<int>>& edges, vector<int>& group) {
        // Step 1: Build adjacency list
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            adj[e[0]].push_back(e[1]);
            adj[e[1]].push_back(e[0]);
        }
        int G = 21; // group labels are 1...20
        vector<vector<int>> subtree_count(G, vector<int>(n, 0));
        vector<int> group_total(G, 0);
        for (int i = 0; i < n; ++i) {
            group_total[group[i]]++;
        }
        // Step 2: For each group, DFS subtree counts
        function<void(int,int,int)> dfs = [&](int u, int p, int g) {
            subtree_count[g][u] = (group[u]==g?1:0);
            for (int v : adj[u]) {
                if (v == p) continue;
                dfs(v, u, g);
                subtree_count[g][u] += subtree_count[g][v];
            }
        };
        for (int g = 1; g < G; ++g) {
            if (group_total[g] > 1) {
                dfs(0, -1, g);
            }
        }
        // Step 3: Calculate contributions for all edges
        long long ans = 0;
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            // To ensure correct parent/child direction, compare subtree sizes
            for (int g = 1; g < G; ++g) {
                if (group_total[g] > 1) {
                    // Always make v the child (smaller subtree) of u
                    if (subtree_count[g][v] > subtree_count[g][u]) swap(u, v);
                    int cnt1 = subtree_count[g][v];
                    int cnt2 = group_total[g] - cnt1;
                    if (cnt1 && cnt2) {
                        ans += 1LL * cnt1 * cnt2;
                    }
                }
            }
        }
        // Each unordered pair is counted once 
        return ans;
    }
};
# @lc code=end