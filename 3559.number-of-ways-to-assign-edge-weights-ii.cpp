#
# @lc app=leetcode id=3559 lang=cpp
#
# [3559] Number of Ways to Assign Edge Weights II
#
# @lc code=start
class Solution {
public:
    const int MOD = 1e9 + 7;
    vector<vector<int>> adj;
    
    bool findPath(int node, int target, int parent, vector<int>& path) {
        path.push_back(node);
        if (node == target) return true;
        
        for (int neighbor : adj[node]) {
            if (neighbor == parent) continue;
            if (findPath(neighbor, target, node, path)) return true;
        }
        
        path.pop_back();
        return false;
    }
    
    long long power(long long base, long long exp) {
        long long result = 1;
        base %= MOD;
        while (exp > 0) {
            if (exp & 1) result = (result * base) % MOD;
            base = (base * base) % MOD;
            exp >>= 1;
        }
        return result;
    }
    
    vector<int> assignEdgeWeights(vector<vector<int>>& edges, vector<vector<int>>& queries) {
        int n = edges.size() + 1;
        adj.resize(n + 1);
        
        for (auto& edge : edges) {
            adj[edge[0]].push_back(edge[1]);
            adj[edge[1]].push_back(edge[0]);
        }
        
        vector<int> answer;
        for (auto& query : queries) {
            int u = query[0], v = query[1];
            vector<int> path;
            findPath(u, v, -1, path);
            
            int numEdges = path.size() - 1;
            if (numEdges == 0) {
                answer.push_back(0);
            } else {
                answer.push_back((int)power(2, numEdges - 1));
            }
        }
        
        return answer;
    }
};
# @lc code=end