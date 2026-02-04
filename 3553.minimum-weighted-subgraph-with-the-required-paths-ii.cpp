# @lc app=leetcode id=3553 lang=cpp
# [3553] Minimum Weighted Subgraph With the Required Paths II

# @lc code=start
class Solution {
public:
    vector<int> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        // Graph adjacency list representation
        unordered_map<int, vector<pair<int, int>>> graph;
        for (const auto& edge : edges) {
            graph[edge[0]].emplace_back(edge[1], edge[2]);
            graph[edge[1]].emplace_back(edge[0], edge[2]);
        }
        
        vector<int> results;
        for (const auto& query : queries) {
            int src1 = query[0], src2 = query[1], dest = query[2];
            
            // Helper function for Dijkstra's algorithm
            auto dijkstra = [&](int start) {
                priority_queue<pair<int, int>, vector<pair<int, int>>, greater<>> pq;
                unordered_map<int, int> dist;
                pq.emplace(0, start);
                dist[start] = 0;
                while (!pq.empty()) {
                    auto [current_dist, u] = pq.top(); pq.pop();
                    if (current_dist > dist[u]) continue;
                    for (auto [v, weight] : graph[u]) {
                        if (dist.find(v) == dist.end() || current_dist + weight < dist[v]) {
                            dist[v] = current_dist + weight;
                            pq.emplace(dist[v], v);
                        }
                    }
                }
                return dist;
            };
            
            // Get distances from src1 and src2
            auto dist_from_src1 = dijkstra(src1);
            auto dist_from_src2 = dijkstra(src2);
            auto dist_from_dest = dijkstra(dest);
            
            int min_weight = INT_MAX;  // Initialize with a large number
            // Find minimum subtree weight that connects both sources to dest
            for (const auto& [node, d_src1] : dist_from_src1) {
                if (dist_from_src2.count(node) && dist_from_dest.count(node)) {												   	                                 	  	    	                  	  	      	                                    	     	     	      	     	    	       	          domi          domi          domi         domi         domi         domi         domi         domi         domi         domi         domi      mitom       mitom       mitom       mitom       mitom       mitom      omes       omes  omes  omes  omes  ome omeomesomesomesomesoemesoeemsomeemesomeemesomeemesomeemesomeemesomeesmomeosmomeosmomeosmomeosmomeosmomeosmomeosmomeosmomemosmomemosmomemosmomemosmomemosmomemosmomemosmomemosmomosmosmosmosmosmosmosmosmosmomosmomosmomosmomosmoosmoosmoosmoosmoosmoosmoosmoosmoosmoosoooomoooomoooomoooomoooowooooowooooowooooowoooowoooowooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo