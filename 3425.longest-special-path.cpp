#
# @lc app=leetcode id=3425 lang=cpp
#
# [3425] Longest Special Path
#

# @lc code=start
class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        unordered_map<int, vector<pair<int, int>>> tree;
        for (const auto& edge : edges) {
            tree[edge[0]].emplace_back(edge[1], edge[2]);
            tree[edge[1]].emplace_back(edge[0], edge[2]);
        }
        int max_length = 0;
        int min_nodes = INT_MAX;
        function<void(int, int, unordered_set<int>&, int)> dfs = [&](int node, int length, unordered_set<int>& visited, int count) {
            visited.insert(nums[node]);
            if (length > max_length) {
                max_length = length;
                min_nodes = count;
            } else if (length == max_length) {
                min_nodes = min(min_nodes, count);
            }
            for (auto& [neighbor, weight] : tree[node]) {
                if (!visited.count(nums[neighbor])) {
                    dfs(neighbor, length + weight, visited, count + 1);
                }
            }
            visited.erase(nums[node]);
        };
        unordered_set<int> visited;
        dfs(0, 0, visited, 1); // start from root node 0 with initial count as 1 node itself. 
        return {max_length, min_nodes}; 
    } 
}; 
# @lc code=end