# @lc code=start
class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        // Initialize adjacency list for tree representation
        unordered_map<int, vector<pair<int, int>>> adj;
        for (const auto& edge : edges) {
            int u = edge[0], v = edge[1], length = edge[2];
            adj[u].emplace_back(v, length);
            adj[v].emplace_back(u, length);
        }
        
        // Variables to track longest path and minimum nodes
        int maxLength = 0;
        int minNodes = INT_MAX;
        
        // Helper function for DFS
        function<void(int, int, int, set<int>&)> dfs = [&](int node, int parent, int currentLength, set<int>& visitedValues) {
            if (visitedValues.count(nums[node])) return; // Ensure unique values
            
            visitedValues.insert(nums[node]);
            bool isLeaf = true;
            
            for (const auto& [nextNode, length] : adj[node]) {
                if (nextNode != parent) { // Avoid revisiting parent node
                    isLeaf = false;
                    dfs(nextNode, node, currentLength + length, visitedValues);
                }
            }
            
            // Update results if at a leaf or end of valid path
            if (isLeaf || currentLength > maxLength) {
                if (currentLength > maxLength) {
                    maxLength = currentLength;
                    minNodes = visitedValues.size();
                } else if (currentLength == maxLength) {
                    minNodes = min(minNodes, static_cast<int>(visitedValues.size()));
                }
            }
            
            visitedValues.erase(nums[node]); // Backtrack
        };
        
        // Start DFS from root node 0 with empty visited values set
        set<int> initialVisitedValues;
        dfs(0, -1, 0, initialVisitedValues);
        
        return {maxLength, minNodes};
    }
};
# @lc code=end