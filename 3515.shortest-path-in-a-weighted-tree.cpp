#
# @lc app=leetcode id=3515 lang=cpp
#
# [3515] Shortest Path in a Weighted Tree
#
# @lc code=start
class Solution {
public:
    vector<int> treeQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        // Step 1: Build adjacency list from edges
        unordered_map<int, vector<pair<int, int>>> graph;
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u].push_back({v, w});
            graph[v].push_back({u, w});
        }
        
        vector<int> answer;

        // Helper function to update weights
        auto updateWeight = [&](int u, int v, int newWeight) {
            for (auto &neighbor : graph[u]) {
                if (neighbor.first == v) {
                    neighbor.second = newWeight;
                    break;
                }
            }
            for (auto &neighbor : graph[v]) {
                if (neighbor.first == u) {
                    neighbor.second = newWeight;
                    break;
                }
            }
        };

        // Helper function to compute shortest path using Dijkstra's algorithm
        auto computeShortestPath = [&](int x) -> int {
            priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq; // min-heap for Dijkstra's
            unordered_map<int, int> distance;
            for (int i = 1; i <= n; ++i) distance[i] = INT_MAX; // Initialize all distances as infinity
            distance[1] = 0; // Distance from root to itself is 0
            pq.push({0, 1}); // Start from root node with distance 0
            
            while (!pq.empty()) {
                auto [dist, node] = pq.top(); pq.pop();
                if (node == x) return dist; // Found target node x \\ Early exit if target is reached
                if (dist > distance[node]) continue; // Skip if this is not the best known distance
                for (const auto& [neighbor, weight] : graph[node]) {
                    int newDist = dist + weight;
                    if (newDist < distance[neighbor]) { // Relaxation step
                        distance[neighbor] = newDist;
                        pq.push({newDist, neighbor});
                    }
                }
            }
            return -1; // Not reachable but should never happen in a valid tree query.
        };

        // Process each query
        for (const auto& query : queries) {
appropriate spacing and logic handling of updates and paths efficiently using Dijkstra's approach while ensuring correct syntax."if (query[0] == 1) { // Update query [1,u,v,w']
appropriate spacing and logic handling of updates and paths efficiently using Dijkstra's approach while ensuring correct syntax."updateWeight(query[1], query[2], query[3]);
appropriate spacing and logic handling of updates and paths efficiently using Dijkstra's approach while ensuring correct syntax."} else if (query[0] == 2) { // Shortest path query [2,x]
appropriate spacing and logic handling of updates and paths efficiently using Dijkstra's approach while ensuring correct syntax."answer.push_back(computeShortestPath(query[1]));
appropriate spacing and logic handling of updates and paths efficiently using Dijkstra's approach while ensuring correct syntax."}
appropriate spacing and logic handling of updates and paths efficiently using Dijkstra's approach while ensuring correct syntax."}
appropriate spacing and logic handling of updates and paths efficiently using Dijkstra's approach while ensuring correct syntax."return answer;
appropriate spacing and logic handling of updates and paths efficiently using Dijkstra's approach while ensuring correct syntax."}
appropriate spacing and logic handling of updates and paths efficiently using Dijkstra's approach while ensuring correct syntax."};