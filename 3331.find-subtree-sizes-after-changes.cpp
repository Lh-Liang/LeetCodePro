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
        vector<vector<int>> adj(n);
        for (int i = 1; i < n; ++i) {
            adj[parent[i]].push_back(i);
        }

        vector<int> new_parent = parent;
        vector<int> last_seen(26, -1);

        // DFS to find new parents based on closest ancestors with same character
        auto findNewParents = [&](auto self, int u) -> void {
            int char_idx = s[u] - 'a';
            int prev_node = last_seen[char_idx];
            
            if (prev_node != -1) {
                new_parent[u] = prev_node;
            }
            
            last_seen[char_idx] = u;
            for (int v : adj[u]) {
                self(self, v);
            }
            last_seen[char_idx] = prev_node; // Backtrack
        };

        findNewParents(findNewParents, 0);

        // Build the new tree structure
        vector<vector<int>> new_adj(n);
        for (int i = 1; i < n; ++i) {
            new_adj[new_parent[i]].push_back(i);
        }

        // DFS to calculate subtree sizes in the new tree
        vector<int> subtree_size(n, 0);
        auto calculateSizes = [&](auto self, int u) -> void {
            subtree_size[u] = 1;
            for (int v : new_adj[u]) {
                self(self, v);
                subtree_size[u] += subtree_size[v];
            }
        };

        calculateSizes(calculateSizes, 0);
        return subtree_size;
    }
};
# @lc code=end