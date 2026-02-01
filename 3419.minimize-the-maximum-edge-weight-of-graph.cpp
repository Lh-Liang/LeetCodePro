#
# @lc app=leetcode id=3419 lang=cpp
#
# [3419] Minimize the Maximum Edge Weight of Graph
#

# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class Solution {
public:
    int minMaxWeight(int n, vector<vector<int>>& edges, int threshold) {
        // Build reversed adjacency list: if u -> v exists, store v -> u
        // This allows us to check if all nodes can reach 0 by seeing if 0 can reach all nodes.
        vector<vector<pair<int, int>>> rev_adj(n);
        int max_w = 0;
        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];
            rev_adj[v].push_back({u, w});
            if (w > max_w) max_w = w;
        }

        // Feasibility check: Can node 0 reach all nodes in reversed graph using weights <= limit?
        auto canReachAll = [&](int limit) -> bool {
            vector<bool> visited(n, false);
            queue<int> q;
            q.push(0);
            visited[0] = true;
            int visited_count = 1;

            while (!q.empty()) {
                int u = q.front();
                q.pop();

                if (visited_count == n) return true;

                for (auto& edge : rev_adj[u]) {
                    int v = edge.first;
                    int w = edge.second;
                    if (w <= limit && !visited[v]) {
                        visited[v] = true;
                        visited_count++;
                        q.push(v);
                    }
                }
            }
            return visited_count == n;
        };

        int low = 1, high = max_w;
        int result = -1;

        // Binary search on the weight limit
        while (low <= high) {
            int mid = low + (high - low) / 2;
            if (canReachAll(mid)) {
                result = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }

        return result;
    }
};
# @lc code=end