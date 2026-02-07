#
# @lc app=leetcode id=3331 lang=cpp
#
# [3331] Find Subtree Sizes After Changes
#

# @lc code=start
class Solution {
public:
    vector<int> findSubtreeSizes(vector<int>& parent, string s) {
        int n = parent.size();
        vector<vector<int>> adj(n);
        vector<int> answer(n, 0);
        unordered_map<char, int> lastSeen;
        
        // Build adjacency list representation of the tree
        for (int i = 1; i < n; ++i) {
            adj[parent[i]].push_back(i);
        }
        
        // Function to find size of subtrees via DFS
        function<int(int)> dfs = [&](int node) {
            int size = 1;
            for (int child : adj[node]) {
                size += dfs(child);
            }
            return answer[node] = size;
        };
        
        // Traverse and find closest ancestor with same character for each node
        for (int i = 1; i < n; ++i) {
            char c = s[i];
            if (lastSeen.count(c)) {
                // Change parent if a matching ancestor exists
                int ancestor = lastSeen[c];
                adj[parent[i]].erase(remove(adj[parent[i]].begin(), adj[parent[i]].end(), i), adj[parent[i]].end());
                adj[ancestor].push_back(i);
                parent[i] = ancestor;
            }
            lastSeen[c] = i;
        }
        
        // Calculate subtree sizes from root using DFS
        dfs(0);

        return answer;
    }
};
# @lc code=end