#
# @lc app=leetcode id=3786 lang=cpp
#
# [3786] Total Sum of Interaction Cost in Tree Groups
#

# @lc code=start
#include <vector>
#include <numeric>

using namespace std;

class Solution {
public:
    long long interactionCosts(int n, vector<vector<int>>& edges, vector<int>& group) {
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        // Group nodes by their group ID
        vector<int> group_counts(21, 0);
        for (int g : group) {
            group_counts[g]++;
        }

        long long total_cost = 0;

        // Since group IDs are small (1 to 20), we can process each group independently
        for (int g = 1; g <= 20; ++g) {
            if (group_counts[g] < 2) continue;

            int target_group = g;
            int total_in_group = group_counts[g];
            
            // DFS to count nodes of the target group in subtrees and calculate edge contributions
            // Using a simple iterative DFS or recursive with a helper
            vector<int> subtree_count(n, 0);
            vector<int> parent(n, -1);
            vector<int> order;
            vector<int> stack = {0};
            parent[0] = -2; // root marker

            while(!stack.empty()) {
                int u = stack.back();
                stack.pop_back();
                order.push_back(u);
                for (int v : adj[u]) {
                    if (parent[v] == -1) {
                        parent[v] = u;
                        stack.push_back(v);
                    }
                }
            }

            // Process in post-order to accumulate subtree counts
            for (int i = n - 1; i >= 0; --i) {
                int u = order[i];
                if (group[u] == target_group) {
                    subtree_count[u]++;
                }
                if (parent[u] >= 0) {
                    subtree_count[parent[u]] += subtree_count[u];
                    // Contribution of edge (u, parent[u])
                    long long count_u = subtree_count[u];
                    total_cost += count_u * (total_in_group - count_u);
                }
            }
        }

        return total_cost;
    }
};
# @lc code=end