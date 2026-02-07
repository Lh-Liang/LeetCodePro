#
# @lc app=leetcode id=3486 lang=cpp
#
# [3486] Longest Special Path II
#

# @lc code=start
class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        unordered_map<int, vector<pair<int,int>>> adjList;
        for (const auto& edge : edges) {
            adjList[edge[0]].emplace_back(edge[1], edge[2]);
            adjList[edge[1]].emplace_back(edge[0], edge[2]);
        }
        vector<int> result = {0, INT_MAX}; // length and min nodes count
        function<void(int, int, unordered_map<int,int>&)> dfs = [&](int node, int parent, unordered_map<int,int>& freq) {
            freq[nums[node]]++;
            bool canRepeat = (freq.size() == nums.size() || (freq.size() == nums.size() - 1 && freq[nums[node]] == 2));
            int maxLength = 0; // max path length from this node
            int minNodes = 0; // min nodes count on this path
            for (const auto& [neighbor, weight] : adjList[node]) {
                if (neighbor == parent) continue; // avoid going back to parent node in undirected tree traverse
                dfs(neighbor, node, freq);
                if (canRepeat) { // valid special path condition met here. Update accordingly. 
                    result[0] = max(result[0], maxLength + weight); 
                    if (maxLength + weight == result[0]) { 
                        result[1] = min(result[1], minNodes + 1); // update minimum only if we reach same path length. 
                    } 
                } 
            } ‘// backtracking after visiting all neighbors on our way back up in recursion ‘// removes current node from frequency count as we move up recursion stack ‘freq[nums[node]]--; ‘if (freq[nums[node]] == 0) freq.erase(nums[node]); ‘}; // calling dfs from root node initially with empty frequency map dfs(0,-1,freq); return result; } }; # @lc code=end