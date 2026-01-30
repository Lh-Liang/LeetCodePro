#
# @lc app=leetcode id=3604 lang=cpp
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#
# @lc code=start
#include <vector>
#include <queue>
#include <climits>
#include <algorithm>

using namespace std;

class Solution {
public:
    struct Edge {
        int to;
        int start;
        int end;
    };

    int minTime(int n, vector<vector<int>>& edges) {
        // Adjacency list to store the directed edges
        vector<vector<Edge>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2], e[3]});
        }

        // minDist[i] stores the minimum time to reach node i
        vector<long long> minDist(n, LLONG_MAX);
        // Min-priority queue for Dijkstra's: {time, node}
        priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> pq;

        // Start at node 0 at time 0
        minDist[0] = 0;
        pq.push({0, 0});

        while (!pq.empty()) {
            auto [d, u] = pq.top();
            pq.pop();

            // Standard Dijkstra optimization
            if (d > minDist[u]) continue;

            // Early exit if we reach the target
            if (u == n - 1) return (int)d;

            for (const auto& edge : adj[u]) {
                // We can use the edge if current time d <= availability end time
                if (d <= (long long)edge.end) {
                    // Earliest start time is max(current time, edge start time)
                    // Arrival time is start time + 1 unit of travel time
                    long long arrival = max(d, (long long)edge.start) + 1;
                    if (arrival < minDist[edge.to]) {
                        minDist[edge.to] = arrival;
                        pq.push({arrival, edge.to});
                    }
                }
            }
        }

        return minDist[n - 1] == LLONG_MAX ? -1 : (int)minDist[n - 1];
    }
};
# @lc code=end