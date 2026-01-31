#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    /**
     * Calculates the total sum of interaction costs (path lengths) for all unordered pairs
     * of nodes belonging to the same group.
     */
    long long interactionCosts(int n, vector<vector<int>>& edges, vector<int>& group) {
        if (n <= 1) return 0;

        // 1. Build the adjacency list for the tree
        vector<vector<int>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }

        // 2. Pre-calculate total node counts for each group label (1 to 20)
        const int MAX_G = 20;
        vector<int> group_totals(MAX_G + 1, 0);
        for (int g : group) {
            group_totals[g]++;
        }

        // 3. Generate a BFS traversal order to facilitate iterative post-order processing
        vector<int> order;
        order.reserve(n);
        vector<int> parent(n, -1);
        queue<int> q;

        q.push(0);
        parent[0] = -2; // Sentinel for root

        while (!q.empty()) {
            int u = q.front();
            q.pop();
            order.push_back(u);
            for (int v : adj[u]) {
                if (parent[v] == -1) {
                    parent[v] = u;
                    q.push(v);
                }
            }
        }

        // 4. Calculate subtree counts and edge contributions bottom-up
        // subtree_counts[u * 21 + g] stores the number of nodes of group g in u's subtree
        vector<int> subtree_counts(n * (MAX_G + 1), 0);
        long long total_interaction_cost = 0;

        // Process nodes in reverse BFS order (leaves to root)
        for (int i = n - 1; i >= 0; --i) {
            int u = order[i];
            int u_off = u * (MAX_G + 1);
            
            // Include the node itself in its group's subtree count
            subtree_counts[u_off + group[u]]++;

            // If not the root, process the edge connecting u to its parent
            if (parent[u] != -2) {
                int p = parent[u];
                int p_off = p * (MAX_G + 1);
                
                for (int g = 1; g <= MAX_G; ++g) {
                    int k = subtree_counts[u_off + g];
                    if (k > 0) {
                        // Contribution of edge (u, p) to group g: k nodes inside * (Total - k) nodes outside
                        total_interaction_cost += (long long)k * (group_totals[g] - k);
                        
                        // Propagate subtree counts to the parent
                        subtree_counts[p_off + g] += k;
                    }
                }
            }
        }

        return total_interaction_cost;
    }
};