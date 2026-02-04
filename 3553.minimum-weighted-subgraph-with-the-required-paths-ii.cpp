#
# @lc app=leetcode id=3553 lang=cpp
#
# [3553] Minimum Weighted Subgraph With the Required Paths II
#

# @lc code=start
class Solution {
public:
    vector<int> minimumWeight(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        // Step 1: Parse input edges to build adjacency list representation of the tree.
        unordered_map<int, vector<pair<int,int>>> adj;
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w}); // because it's undirected
        }
        
        vector<int> answer;
        // Step 2: Implement BFS/DFS to find paths from src1 and src2 to dest for each query.
        function<int(int,int)> findPathWeight = [&](int src, int dest) {
            unordered_map<int, int> dist; // node -> distance from src
            priority_queue<pair<int,int>, vector<pair<int,int>>, greater<>> pq;
            pq.push({0, src}); // (distance, node) starting from src with distance 0
            dist[src] = 0;
            while (!pq.empty()) {
                auto [d, u] = pq.top(); pq.pop();
                if (u == dest) return d; // found shortest path to dest
                if (d > dist[u]) continue; // skip if this is not the shortest known path to u
                for (auto &[v, w] : adj[u]) {
                    if (dist.find(v) == dist.end() || d + w < dist[v]) {
                        dist[v] = d + w;
                        pq.push({dist[v], v});
                    } 
                } 
            } 
            return INT_MAX; // dest not reachable from src in this subtree context. 
        }; 
        
        for (const auto& query : queries) { 
            int src1 = query[0], src2 = query[1], dest = query[2]; 
            int totalWeight = findPathWeight(src1, dest) + findPathWeight(src2, dest); 
            answer.push_back(totalWeight); 
        } 
        return answer; 
n    } 
n}; 
n# @lc code=end