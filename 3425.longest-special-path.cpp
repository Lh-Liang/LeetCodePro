#
# @lc app=leetcode id=3425 lang=cpp
#
# [3425] Longest Special Path
#
# @lc code=start
#include <vector>
#include <unordered_set>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        vector<vector<pair<int, int>>> tree(n);
        for (const auto& e : edges) {
            int u = e[0], v = e[1], l = e[2];
            tree[u].emplace_back(v, l);
            tree[v].emplace_back(u, l);
        }

        int maxLen = 0, minNodes = 1;
        unordered_set<int> seen;
        function<void(int, int, int, int)> dfs = [&](int node, int parent, int curLen, int curNodes) {
            if (seen.count(nums[node])) return;
            seen.insert(nums[node]);
            if (curLen > maxLen) {
                maxLen = curLen;
                minNodes = curNodes;
            } else if (curLen == maxLen) {
                minNodes = min(minNodes, curNodes);
            }
            for (auto& [nei, l] : tree[node]) {
                if (nei != parent) {
                    dfs(nei, node, curLen + l, curNodes + 1);
                }
            }
            seen.erase(nums[node]);
        };
        for (int i = 0; i < n; ++i) {
            seen.clear();
            dfs(i, -1, 0, 1);
        }
        return {maxLen, minNodes};
    }
};
# @lc code=end