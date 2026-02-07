# \@lc app=leetcode id=3553 lang=cpp
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#
# \@lc code=start
#include <vector>
#include <queue>
#include <unordered_map>
#include <limits>
using namespace std;

class Solution {
public:
    vector<int> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1; // n is number of nodes since edges are n-1
        vector<unordered_map<int, int>> graph(n);

        // Build graph from edges
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u][v] = w;
            graph[v][u] = w;
        }

        vector<int> result;
        // Lambda function to calculate shortest path using Dijkstra's algorithm from a start node
        auto dijkstra_shortest_path = [&](int start) {
            vector<int> dist(n, numeric_limits<int>::max());
            priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
            pq.push({0, start});
            dist[start] = 0;
            while (!pq.empty()) {
                auto [currentDist, node] = pq.top(); pq.pop();
                if (currentDist > dist[node]) continue;
                for (const auto& [neighbor, weight] : graph[node]) {
                    if (dist[node] + weight < dist[neighbor]) {
                        dist[neighbor] = dist[node] + weight;
                        pq.push({dist[neighbor], neighbor});
                    }
                }
            }
            return dist;
        };

        for (const auto& query : queries) {
data}
data}
data// \@lc code=end