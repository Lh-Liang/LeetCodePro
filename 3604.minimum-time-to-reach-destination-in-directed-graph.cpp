#
# @lc app=leetcode id=3604 lang=cpp
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#

# @lc code=start
#include <vector>
#include <queue>
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
        // Build adjacency list
        vector<vector<Edge>> adj(n);
        for (const auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2], e[3]});
        }

        // Dijkstra's algorithm
        // dist[i] stores the earliest time we can reach node i
        const int INF = 2000000000; // 2e9 is safe for the expected maximum time
        vector<int> dist(n, INF);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

        dist[0] = 0;
        pq.push({0, 0});

        while (!pq.empty()) {
            pair<int, int> current = pq.top();
            int d = current.first;
            int u = current.second;
            pq.pop();

            // If we already found a faster way to reach u, skip
            if (d > dist[u]) continue;

            // If we reached the destination node, return the time
            if (u == n - 1) return d;

            for (const auto& edge : adj[u]) {
                // Can only use the edge if current time is not past the end time
                if (d <= edge.end) {
                    // Earliest time to start travel is max(current time, edge start time)
                    int startTime = max(d, edge.start);
                    int arrivalTime = startTime + 1;
                    
                    // If this path is faster, update and push to priority queue
                    if (arrivalTime < dist[edge.to]) {
                        dist[edge.to] = arrivalTime;
                        pq.push({arrivalTime, edge.to});
                    }
                }
            }
        }

        // If node n-1 is unreachable
        return -1;
    }
};
# @lc code=end