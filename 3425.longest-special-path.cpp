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
        vector<vector<pair<int, int>>> tree(n); // node, edge length
        for (auto& e : edges) {
            int u = e[0], v = e[1], l = e[2];
            tree[u].emplace_back(v, l);
            tree[v].emplace_back(u, l);
        }
        int maxLength = 0;
        int minNodes = 1;
        unordered_map<int, int> valueCount;
        function<void(int, int, int, int)> dfs = [&](int node, int parent, int currLen, int nodeCount) {
            valueCount[nums[node]]++;
            if (currLen > maxLength) {
                maxLength = currLen;
                minNodes = nodeCount;
            } else if (currLen == maxLength) {
                minNodes = min(minNodes, nodeCount);
            }
            for (auto& [nei, w] : tree[node]) {
                if (nei == parent) continue;
                if (valueCount[nums[nei]] == 0) {
                    dfs(nei, node, currLen + w, nodeCount + 1);
                }
            }
            valueCount[nums[node]]--;
        };
        dfs(0, -1, 0, 1);
        return {maxLength, minNodes};
    }
};
# @lc code=end