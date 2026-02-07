# @lc code=start
class Solution {
public:
    vector<int> treeQueries(int n, vector<vector<int>>& edges, vector<vector<int>>& queries) {
        unordered_map<int, vector<pair<int, int>>> graph;
        map<pair<int, int>, int> edge_weights;
        
        // Build graph and store initial weights
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            graph[u].emplace_back(v, w);
            graph[v].emplace_back(u, w);
            edge_weights[{min(u,v), max(u,v)}] = w;
        }
        
        vector<int> answer;
        unordered_map<int, int> distances; // Store computed distances from root

        // DFS function to calculate distances from root (node 1)
        function<void(int, int)> dfs = [&](int node, int dist) {
            distances[node] = dist;
            for (auto& [neighbor, weight] : graph[node]) {
                if (!distances.count(neighbor)) {
                    dfs(neighbor, dist + weight);
                }
            }
        };

        // Initially compute all distances from root if needed
        bool isFirstQuery = true;

        for (const auto& query : queries) {
            if (query[0] == 1) { // Update edge weight [1,u,v,w']
                int u = query[1], v = query[2], new_weight = query[3];
                auto edge_key = make_pair(min(u,v), max(u,v));
                if (edge_weights[edge_key] != new_weight) {
                    // Update both sides in graph adjacency list
                    for (auto& [neighbor, weight] : graph[u]) {
                        if (neighbor == v) { weight = new_weight; break; }
                    }
                    for (auto& [neighbor, weight] : graph[v]) {
                        if (neighbor == u) { weight = new_weight; break; }
                    }
                    // Update stored edge weight
                    edge_weights[edge_key] = new_weight;
                    isFirstQuery = true; // Reset flag to recompute distances on next query type [2,x]
                }
            } else { // Shortest path query [2,x]
                int x = query[1];
                if (isFirstQuery) { // Recompute all distances only when necessary
                    distances.clear();
                    dfs(1, 0); // Compute distances from root node 1 initially or after an update
                    isFirstQuery = false;
                }
                answer.push_back(distances[x]);
            }
        }

        return answer;
    }
m};
m# @lc code=end