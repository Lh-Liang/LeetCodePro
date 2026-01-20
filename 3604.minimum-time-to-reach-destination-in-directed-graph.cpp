#
# @lc app=leetcode id=3604 lang=cpp
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
#include <vector>
#include <queue>
#include <tuple>
#include <algorithm>
#include <climits>

using namespace std;

class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges) {
        // Adjacency list: u -> list of {v, start, end}
        vector<vector<tuple<int, int, int>>> adj(n);
        for (const auto& edge : edges) {
            adj[edge[0]].emplace_back(edge[1], edge[2], edge[3]);
        }

        // Dijkstra's algorithm
        // min_time[i] stores the minimum time to reach node i
        vector<int> min_time(n, INT_MAX);
        // Priority queue stores {current_time, u}, ordered by current_time ascending
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        min_time[0] = 0;
        pq.push({0, 0});

        while (!pq.empty()) {
            auto [t, u] = pq.top();
            pq.pop();

            if (t > min_time[u]) continue;
            if (u == n - 1) return t;

            for (const auto& [v, start, end] : adj[u]) {
                // We arrived at u at time t.
                // We can take the edge if we leave at time t_departure such that:
                // 1. t_departure >= t (we can't travel back in time)
                // 2. start <= t_departure <= end
                
                // If current time is already past the end of the window, we can't use this edge.
                if (t > end) continue;

                // Calculate earliest departure time
                int t_departure = max(t, start);
                
                // Arrival time at v is departure time + 1 unit of traversal
                int t_arrival = t_departure + 1;

                if (t_arrival < min_time[v]) {
                    min_time[v] = t_arrival;
                    pq.push({t_arrival, v});
                }
            }
        }

        return -1;
    }
};
# @lc code=end