#
# @lc app=leetcode id=3419 lang=cpp
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        // We need to find the minimum weight W such that if we only consider edges
        // with weight <= W, node 0 is reachable from all other nodes.
        // Note: The threshold constraint (out-degree <= threshold) is always satisfiable
        // if reachability is satisfiable, because we can just pick a spanning tree 
        // directed towards 0 (where every node != 0 has out-degree 1).
        // Since threshold >= 1, out-degree 1 is always allowed.

        // To check reachability efficiently, we can use the reversed graph.
        // If in the reversed graph, node 0 can reach all other nodes, then in the
        // original graph, all other nodes can reach node 0.

        // 1. Build adjacency list for the reversed graph: adj[v] = {u, w} means u->v with weight w in original.
        vector<vector<pair<int, int>>> reverse_adj(n);
        int max_w = 0;
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            reverse_adj[v].push_back({u, w});
            max_w = max(max_w, w);
        }

        // Helper function for BFS
        auto check = [&](int max_weight_limit) -> bool {
            vector<bool> visited(n, false);
            queue<int> q;
            
            visited[0] = true;
            q.push(0);
            int count = 1;

            while (!q.empty()) {
                int curr = q.front();
                q.pop();

                if (count == n) return true; // Optimization

                for (const auto& neighbor : reverse_adj[curr]) {
                    int next_node = neighbor.first;
                    int weight = neighbor.second;

                    if (!visited[next_node] && weight <= max_weight_limit) {
                        visited[next_node] = true;
                        count++;
                        q.push(next_node);
                    }
                }
            }
            return count == n;
        };

        // Collect all unique weights for binary search or just use range [1, 10^6]
        // Using sorted unique weights is slightly faster but range binary search is simpler to implement.
        // Given constraints, distinct weights might be up to E. Let's use sorted unique weights.
        vector<int> weights;
        weights.reserve(edges.size());
        for(const auto& e : edges) weights.push_back(e[2]);
        sort(weights.begin(), weights.end());
        weights.erase(unique(weights.begin(), weights.end()), weights.end());

        if (weights.empty()) return -1; // No edges, impossible if n > 1. But problem says n >= 2.

        int left = 0;
        int right = weights.size() - 1;
        int ans = -1;

        while (left <= right) {
            int mid_idx = left + (right - left) / 2;
            int w = weights[mid_idx];
            
            if (check(w)) {
                ans = w;
                right = mid_idx - 1;
            } else {
                left = mid_idx + 1;
            }
        }

        return ans;
    }
};
# @lc code=end