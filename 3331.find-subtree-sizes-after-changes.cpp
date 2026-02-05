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
        vector<int> new_parent = parent;
        vector<vector<int>> tree(n);
        // Build original tree
        for (int i = 1; i < n; ++i) {
            tree[parent[i]].push_back(i);
        }
        // For each character, maintain a stack of (node, depth)
        unordered_map<char, vector<int>> char_stack;
        vector<int> depth(n, 0);
        function<void(int, int)> dfs = [&](int u, int d) {
            depth[u] = d;
            char c = s[u];
            char_stack[c].push_back(u);
            // For all children
            for (int v : tree[u]) {
                // Only process for x != 0
                if (v == 0) continue;
                // Find closest ancestor with same character
                int closest = -1;
                if (!char_stack[c].empty()) {
                    // The last element in stack is the closest ancestor
                    closest = char_stack[c].back();
                }
                // But we push u before processing children, so for v, ancestor is char_stack[c][size-2] (since char_stack[c][size-1]==u==parent of v)
                if (char_stack[c].size() >= 2) {
                    closest = char_stack[c][char_stack[c].size() - 2];
                } else {
                    closest = -1;
                }
                if (closest != -1) {
                    new_parent[v] = closest;
                }
                dfs(v, d + 1);
            }
            char_stack[c].pop_back();
        };
        dfs(0, 0);
        // Build new tree
        vector<vector<int>> new_tree(n);
        for (int i = 1; i < n; ++i) {
            new_tree[new_parent[i]].push_back(i);
        }
        // Compute subtree sizes
        vector<int> ans(n, 0);
        function<int(int)> dfs2 = [&](int u) {
            int sz = 1;
            for (int v : new_tree[u]) {
                sz += dfs2(v);
            }
            ans[u] = sz;
            return sz;
        };
        dfs2(0);
        return ans;
    }
};
# @lc code=end