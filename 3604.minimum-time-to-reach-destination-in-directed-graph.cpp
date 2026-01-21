#
# @lc app=leetcode id=3604 lang=cpp
#
# [3604] Minimum Time to Reach Destination in Directed Graph
#
# @lc code=start
class Solution {
public:
    int minTime(int n, vector<vector<int>>& edges) {
        // Build adjacency list
        vector<vector<tuple<int, int, int>>> graph(n);
        for (const auto& e : edges) {
            graph[e[0]].push_back({e[1], e[2], e[3]});
        }
        
        // Dijkstra's algorithm
        vector<int> dist(n, INT_MAX);
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
        
        dist[0] = 0;
        pq.push({0, 0}); // {time, node}
        
        while (!pq.empty()) {
            auto [time, node] = pq.top();
            pq.pop();
            
            // Early return if we reached the destination
            if (node == n - 1) return time;
            
            // Skip if we've already found a better path to this node
            if (time > dist[node]) continue;
            
            // Explore all outgoing edges
            for (const auto& [next, start, end] : graph[node]) {
                if (time <= end) { // We can potentially use this edge
                    int arrival = max(time, start) + 1;
                    if (arrival < dist[next]) {
                        dist[next] = arrival;
                        pq.push({arrival, next});
                    }
                }
            }
        }
        
        return -1; // Cannot reach destination
    }
};
# @lc code=end