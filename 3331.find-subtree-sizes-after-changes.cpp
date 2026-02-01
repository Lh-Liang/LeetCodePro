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

        vector<int> new_parent(n);
        new_parent[0] = -1;
        vector<int> last_seen(26, -1);

        // DFS to find new parents based on closest ancestor with same character
        auto find_new_parents = [&](auto self, int u) -> void {
            int char_idx = s[u] - 'a';
            int prev_node = last_seen[char_idx];
            
            if (u != 0) {
                if (prev_node != -1) {
                    new_parent[u] = prev_node;
                } else {
                    new_parent[u] = parent[u];
                }
            }

            int old_val = last_seen[char_idx];
            last_seen[char_idx] = u;
            for (int v : adj[u]) {
                self(self, v);
            }
            last_seen[char_idx] = old_val; // backtrack
        };

        find_new_parents(find_new_parents, 0);

        // Build the new tree
        vector<vector<int>> new_adj(n);
        for (int i = 1; i < n; ++i) {
            new_adj[new_parent[i]].push_back(i);
        }

        vector<int> ans(n, 0);
        
        // DFS to calculate subtree sizes in the new tree
        auto calculate_sizes = [&](auto self, int u) -> int {
            int size = 1;
            for (int v : new_adj[u]) {
                size += self(self, v);
            }
            ans[u] = size;
            return size;
        };

        calculate_sizes(calculate_sizes, 0);

        return ans;
    }
};
# @lc code=end