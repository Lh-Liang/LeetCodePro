#
# @lc app=leetcode id=3331 lang=cpp
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> adj(n);
        for (int i = 1; i < n; ++i) {
            adj[parent[i]].push_back(i);
        }
        vector<int> new_parent(n);
        vector<int> last_pos(26, -1);
        auto dfs = [&](auto&& self, int node, int par) -> void {
            int idx = s[node] - 'a';
            int y = last_pos[idx];
            if (node != 0 && y != -1) {
                new_parent[node] = y;
            } else {
                new_parent[node] = par;
            }
            int prev = last_pos[idx];
            last_pos[idx] = node;
            for (int child : adj[node]) {
                if (child != par) {
                    self(self, child, node);
                }
            }
            last_pos[idx] = prev;
        };
        dfs(dfs, 0, -1);
        vector<vector<int>> new_adj(n);
        for (int i = 1; i < n; ++i) {
            new_adj[new_parent[i]].push_back(i);
        }
        vector<int> sz(n);
        auto comp = [&](auto&& self, int node) -> int {
            sz[node] = 1;
            for (int child : new_adj[node]) {
                sz[node] += self(self, child);
            }
            return sz[node];
        };
        comp(comp, 0);
        return sz;
    }
};
# @lc code=end