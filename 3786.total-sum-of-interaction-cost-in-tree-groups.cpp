#
# @lc app=leetcode id=3786 lang=cpp
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
class Solution {
public:
    long long interactionCosts(int n, vector<vector<int>>& edges, vector<int>& group) {
        vector<vector<int>> adj(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1];
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        vector<long long> total(21, 0LL);
        for (int i = 0; i < n; i++) {
            total[group[i]]++;
        }
        vector<long long> contrib(21, 0LL);
        std::function<vector<long long>(int, int)> dfs = [&](int node, int par) -> vector<long long> {
            vector<long long> cnt(21, 0LL);
            cnt[group[node]] = 1LL;
            for (int child : adj[node]) {
                if (child == par) continue;
                vector<long long> child_cnt = dfs(child, node);
                for (int g = 1; g <= 20; g++) {
                    long long sz = child_cnt[g];
                    contrib[g] += sz * (total[g] - sz);
                }
                for (int g = 1; g <= 20; g++) {
                    cnt[g] += child_cnt[g];
                }
            }
            return cnt;
        };
        dfs(0, -1);
        long long ans = 0;
        for (int g = 1; g <= 20; g++) {
            ans += contrib[g];
        }
        return ans;
    }
};
# @lc code=end