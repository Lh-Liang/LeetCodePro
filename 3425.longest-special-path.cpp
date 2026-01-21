#
# @lc app=leetcode id=3425 lang=cpp
#
# [3425] Longest Special Path
#
# @lc code=start
class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int, int>>> graph(n);
        
        for (auto& edge : edges) {
            int u = edge[0], v = edge[1], len = edge[2];
            graph[u].push_back({v, len});
            graph[v].push_back({u, len});
        }
        
        int maxLen = 0;
        int minNodes = 1;
        
        vector<int> path;
        vector<int> edgeLens;
        
        function<void(int, int)> dfs = [&](int node, int parent) {
            path.push_back(node);
            
            unordered_set<int> seenValues;
            int pathLen = 0;
            
            for (int i = path.size() - 1; i >= 0; i--) {
                int val = nums[path[i]];
                if (seenValues.count(val)) break;
                seenValues.insert(val);
                
                int nodes = path.size() - i;
                
                if (pathLen > maxLen || (pathLen == maxLen && nodes < minNodes)) {
                    maxLen = pathLen;
                    minNodes = nodes;
                }
                
                if (i > 0) {
                    pathLen += edgeLens[i - 1];
                }
            }
            
            for (auto [neighbor, edgeLen] : graph[node]) {
                if (neighbor != parent) {
                    edgeLens.push_back(edgeLen);
                    dfs(neighbor, node);
                    edgeLens.pop_back();
                }
            }
            
            path.pop_back();
        };
        
        dfs(0, -1);
        
        return {maxLen, minNodes};
    }
};
# @lc code=end