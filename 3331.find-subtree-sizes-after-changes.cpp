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
        vector<int> answer(n, 1); // Each node is initially its own subtree of size 1.
        vector<vector<int>> adj(n); // Adjacency list for tree representation.
        for(int i = 1; i < n; ++i) {
            adj[parent[i]].push_back(i);
        }
        vector<vector<int>> char_ancestors(26); // Store ancestors by character.
        function<void(int)> dfs = [&](int node) {
            int c_index = s[node] - 'a';
            char_ancestors[c_index].push_back(node); // Add current node to its character list.
            for(int &child : adj[node]) {
                int closest_ancestor = -1; // Track closest ancestor with same char.
                if(!char_ancestors[c_index].empty()) {
                    closest_ancestor = char_ancestors[c_index].back(); // Closest ancestor with same char.
                }
                dfs(child); // Recursively process children.
                if(closest_ancestor != -1 && closest_ancestor != node) {
                    parent[child] = closest_ancestor; // Reassign parent if valid ancestor found. 
                } 
            }              char_ancestors[c_index].pop_back(); // Remove current node from its character list post processing.          };          dfs(0); // Start DFS from root node.          vector<vector<int>> final_adj(n);          for(int i = 1; i < n; ++i) { 	final_adj[parent[i]].push_back(i);          }           function<int(int)> calculate_subtree_sizes = [&](int node) -> int { 	int size = 1; 	for(int &child : final_adj[node]) { 	size += calculate_subtree_sizes(child); 	} 	answer[node] = size; 	return size;           };           calculate_subtree_sizes(0); // Calculate subtree sizes in final tree structure from root.           return answer;       }   }; # @lc code=end