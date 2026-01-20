#include <vector>
#include <string>

using namespace std;

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

        vector<int> new_parent = parent;
        vector<int> last_seen(26, -1);

        // Step 1: Find new parents based on the original tree structure
        dfs_find_parents(0, adj, s, last_seen, new_parent);

        // Step 2: Build the new tree structure based on updated parents
        vector<vector<int>> new_adj(n);
        for (int i = 1; i < n; ++i) {
            new_adj[new_parent[i]].push_back(i);
        }

        // Step 3: Calculate subtree sizes in the modified tree
        vector<int> subtree_size(n, 0);
        dfs_calc_sizes(0, new_adj, subtree_size);

        return subtree_size;
    }

private:
    /**
     * Traverses the original tree to find the closest ancestor with the same character.
     */
    void dfs_find_parents(int u, const vector<vector<int>>& adj, const string& s, 
                          vector<int>& last_seen, vector<int>& new_parent) {
        int char_idx = s[u] - 'a';
        int prev_node = last_seen[char_idx];
        
        if (prev_node != -1) {
            new_parent[u] = prev_node;
        }
        
        // Update last_seen for current character
        last_seen[char_idx] = u;
        for (int v : adj[u]) {
            dfs_find_parents(v, adj, s, last_seen, new_parent);
        }
        // Backtrack: restore previous last_seen value
        last_seen[char_idx] = prev_node;
    }

    /**
     * Traverses the new tree to calculate subtree sizes.
     */
    int dfs_calc_sizes(int u, const vector<vector<int>>& new_adj, vector<int>& subtree_size) {
        int size = 1;
        for (int v : new_adj[u]) {
            size += dfs_calc_sizes(v, new_adj, subtree_size);
        }
        subtree_size[u] = size;
        return size;
    }
};
# @lc code=end