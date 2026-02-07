# @lc app=leetcode id=3373 lang=cpp
#
# [3373] Maximize the Number of Target Nodes After Connecting Trees II
#
# @lc code=start
class Solution {
public:
    vector<int> maxTargetNodes(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        // Convert edge lists to adjacency lists for both trees
        int n = edges1.size() + 1;
        int m = edges2.size() + 1;
        vector<vector<int>> adj1(n);
        vector<vector<int>> adj2(m);
        
        for(auto& edge : edges1) {
            adj1[edge[0]].push_back(edge[1]);
            adj1[edge[1]].push_back(edge[0]);
        }
        
        for(auto& edge : edges2) {
            adj2[edge[0]].push_back(edge[1]);
            adj2[edge[1]].push_back(edge[0]);
        }
        
        // Function to calculate depths using BFS
        auto calculateDepths = [](const vector<vector<int>>& adj, int root) {
            vector<int> depth(adj.size(), -1);
            queue<int> q;
            q.push(root);
            depth[root] = 0;
            while (!q.empty()) {
                int node = q.front(); q.pop();
                for(int neighbor : adj[node]) {
                    if(depth[neighbor] == -1) { // not visited
                        depth[neighbor] = depth[node] + 1;
                        q.push(neighbor);
                    }
                }
            }
            return depth;
        };

        // Calculate depths from any root (say node 0)
        vector<int> depth1 = calculateDepths(adj1, 0);
        vector<int> depth2 = calculateDepths(adj2, 0);

        // Compute maximum target nodes for each node in first tree
        vector<int> result(n, m); // default max targets are total m nodes since they are all reachable initially

        // For each node in tree 1, determine max targetable nodes by connecting it to a node in tree 2
        for (int i = 0; i < n; ++i) {    int maxTargets = m; // default assumption each connection makes all m nodes reachable as targets initially    result[i] = maxTargets;}return result;}