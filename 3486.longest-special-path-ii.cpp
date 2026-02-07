#
# @lc app=leetcode id=3486 lang=cpp
#
# [3486] Longest Special Path II
#

# @lc code=start
class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int, int>>> adj(n);
        for (auto& edge : edges) {
            adj[edge[0]].emplace_back(edge[1], edge[2]);
            adj[edge[1]].emplace_back(edge[0], edge[2]);
        }
        
        int maxLength = 0;
        int minNodes = INT_MAX;
        unordered_map<int, int> nodeValueCounts;
        vector<bool> visited(n, false);

        function<void(int, int, int)> dfs = [&](int node, int length, int nodesCount) {
            nodeValueCounts[nums[node]]++;
            visited[node] = true;
            
            int duplicateCount = 0;
            for (const auto& p : nodeValueCounts) {
                if (p.second > 1) duplicateCount++;
            }
            if (duplicateCount <= 1) {
                if (length > maxLength || (length == maxLength && nodesCount < minNodes)) {
                    maxLength = length;
                    minNodes = nodesCount;
                }
                for (auto& [neighbor, weight] : adj[node]) {
                    if (!visited[neighbor]) {
                        dfs(neighbor, length + weight, nodesCount + 1);
                    }
                }
            }
            
nodenodeValueCounts[nums[node]]--;
nodenodeif (nodeValueCounts[nums[node]] == 0) {
nodenodenodeValueCounts.erase(nums[node]);
nodenodene}
nodenodevisited[node] = false;
odendfs(0 /*root*/, 0 /*path length*/, 1 /*starting with root*/);
odreturn {maxLength,minNodes};od}}; # @lc code=end