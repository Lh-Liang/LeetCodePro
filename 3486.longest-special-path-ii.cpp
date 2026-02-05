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
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            adj[u].push_back({v, w});
            adj[v].push_back({u, w});
        }
        unordered_map<int, int> count;
        int maxLen = 0, minNodes = INT_MAX;
        function<void(int,int,int,int,bool)> dfs = [&](int u, int parent, int currLen, int currNodes, bool dupUsed) {
            count[nums[u]]++;
            if (count[nums[u]] == 2 && dupUsed) {
                count[nums[u]]--;
                return;
            }
            bool newDupUsed = dupUsed || (count[nums[u]] == 2);
            // Update result if at a leaf or at every node
            if (currLen > maxLen) {
                maxLen = currLen;
                minNodes = currNodes;
            } else if (currLen == maxLen) {
                minNodes = min(minNodes, currNodes);
            }
            for (auto& [v, w] : adj[u]) {
                if (v == parent) continue;
                dfs(v, u, currLen + w, currNodes + 1, newDupUsed);
            }
            count[nums[u]]--;
        };
        dfs(0, -1, 0, 1, false);
        return {maxLen, minNodes};
    }
};
# @lc code=end