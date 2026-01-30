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
private:
    // DFS to find the new parent for each node based on the original tree
    void findNewParents(int u, const string& s, const vector<int>& parent, 
                        const vector<vector<int>>& orig_adj, 
                        vector<int>& new_parents, vector<int>& last_occurrence) {
        int char_idx = s[u] - 'a';
        int prev_node = last_occurrence[char_idx];
        
        // The root's parent remains -1. For others, use the closest ancestor with same char
        if (u != 0) {
            new_parents[u] = (prev_node != -1) ? prev_node : parent[u];
        }
        
        int old_val = last_occurrence[char_idx];
        last_occurrence[char_idx] = u;
        
        for (int v : orig_adj[u]) {
            findNewParents(v, s, parent, orig_adj, new_parents, last_occurrence);
        }
        
        // Backtrack to restore the state for other branches
        last_occurrence[char_idx] = old_val;
    }

    // DFS to calculate subtree sizes in the modified tree
    int calculateSubtreeSizes(int u, const vector<vector<int>>& new_adj, vector<int>& subtree_size) {
        int size = 1;
        for (int v : new_adj[u]) {
            size += calculateSubtreeSizes(v, new_adj, subtree_size);
        }
        return subtree_size[u] = size;
    }

public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        if (n == 0) return {};

        // 1. Build original adjacency list
        vector<vector<int>> orig_adj(n);
        for (int i = 1; i < n; ++i) {
            orig_adj[parent[i]].push_back(i);
        }

        // 2. Determine new parents based on original tree ancestors
        vector<int> new_parents(n, -1);
        vector<int> last_occurrence(26, -1);
        findNewParents(0, s, parent, orig_adj, new_parents, last_occurrence);

        // 3. Build new adjacency list based on updated parents
        vector<vector<int>> new_adj(n);
        for (int i = 1; i < n; ++i) {
            new_adj[new_parents[i]].push_back(i);
        }

        // 4. Compute subtree sizes in the new tree
        vector<int> subtree_size(n);
        calculateSubtreeSizes(0, new_adj, subtree_size);

        return subtree_size;
    }
};
# @lc code=end