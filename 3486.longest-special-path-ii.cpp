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
        vector<vector<pair<int, int>>> tree(n);
        for (auto& e : edges) {
            int u = e[0], v = e[1], w = e[2];
            tree[u].emplace_back(v, w);
            tree[v].emplace_back(u, w);
        }
        unordered_map<int, int> cnt;
        int max_len = 0, min_nodes = INT_MAX;
        // DFS with explicit state management and restoration
        function<void(int,int,int,int,int)> dfs = [&](int u, int parent, int curr_len, int nodes, int duplicate) {
            cnt[nums[u]]++;
            bool inc_duplicate = false;
            if (cnt[nums[u]] == 2) {
                duplicate++;
                inc_duplicate = true;
            }
            // Only proceed if at most one value appears twice
            if (duplicate <= 1) {
                if (curr_len > max_len) {
                    max_len = curr_len;
                    min_nodes = nodes;
                } else if (curr_len == max_len) {
                    min_nodes = min(min_nodes, nodes);
                }
                for (auto& [v, w] : tree[u]) {
                    if (v != parent) {
                        dfs(v, u, curr_len + w, nodes + 1, duplicate);
                    }
                }
            }
            // Restore state for backtracking
            if (inc_duplicate) duplicate--;
            cnt[nums[u]]--;
        };
        dfs(0, -1, 0, 1, 0);
        return {max_len, min_nodes};
    }
};
# @lc code=end