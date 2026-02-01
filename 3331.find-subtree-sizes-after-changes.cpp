#
# @lc app=leetcode id=3331 lang=cpp
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
#include <vector>
#include <string>

using namespace std;

class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> original_adj(n);
        for (int i = 1; i < n; ++i) {
            original_adj[parent[i]].push_back(i);
        }

        vector<int> current_path_chars(26, -1);
        vector<int> new_parent = parent;

        // First DFS: Determine new parents based on original structure
        auto update_parents = [&](auto self, int u) -> void {
            int char_idx = s[u] - 'a';
            int prev_ancestor = current_path_chars[char_idx];
            
            if (prev_ancestor != -1) {
                new_parent[u] = prev_ancestor;
            }
            
            int temp = current_path_chars[char_idx];
            current_path_chars[char_idx] = u;
            
            for (int v : original_adj[u]) {
                self(self, v);
            }
            
            current_path_chars[char_idx] = temp; // Backtrack
        };
        update_parents(update_parents, 0);

        // Build the new tree structure
        vector<vector<int>> new_adj(n);
        for (int i = 1; i < n; ++i) {
            new_adj[new_parent[i]].push_back(i);
        }

        // Second DFS: Calculate subtree sizes
        vector<int> ans(n, 0);
        auto calculate_size = [&](auto self, int u) -> int {
            int size = 1;
            for (int v : new_adj[u]) {
                size += self(self, v);
            }
            return ans[u] = size;
        };
        calculate_size(calculate_size, 0);

        return ans;
    }
};
# @lc code=end