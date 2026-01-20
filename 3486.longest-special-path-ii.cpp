#include <vector>
#include <algorithm>
#include <map>

using namespace std;

#
# @lc app=leetcode id=3486 lang=cpp
#
# [3486] Longest Special Path II
#

# @lc code=start
class Solution {
public:
    long long max_len = 0;
    int min_nodes = 1;
    vector<int> path_p0;
    vector<long long> path_dist;
    vector<vector<int>> pos;
    vector<vector<pair<int, int>>> adj;
    vector<int> node_nums;

    void dfs(int u, int p, int depth, long long dist, int p0, int p1) {
        int val = node_nums[u];
        int i1 = pos[val].empty() ? -1 : pos[val].back();
        int i2 = (pos[val].size() < 2) ? -1 : pos[val][pos[val].size() - 2];

        int cur_p0 = max(p0, i1 + 1);
        int cur_p1;
        if (i1 == -1) {
            cur_p1 = p1;
        } else {
            int start_with_val_dup = max(i2 + 1, path_p0[i1]);
            int start_with_other_dup = max(i1 + 1, p1);
            cur_p1 = min(start_with_val_dup, start_with_other_dup);
        }

        path_p0[depth] = cur_p0;
        path_dist[depth] = dist;

        long long current_path_len = dist - path_dist[cur_p1];
        int current_path_nodes = depth - cur_p1 + 1;

        if (current_path_len > max_len) {
            max_len = current_path_len;
            min_nodes = current_path_nodes;
        } else if (current_path_len == max_len) {
            min_nodes = min(min_nodes, current_path_nodes);
        }

        pos[val].push_back(depth);
        for (auto& edge : adj[u]) {
            if (edge.first != p) {
                dfs(edge.first, u, depth + 1, dist + edge.second, cur_p0, cur_p1);
            }
        }
        pos[val].pop_back();
    }

    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        adj.assign(n, vector<pair<int, int>>());
        for (auto& edge : edges) {
            adj[edge[0]].push_back({edge[1], edge[2]});
            adj[edge[1]].push_back({edge[0], edge[2]});
        }
        node_nums = nums;
        path_p0.assign(n, 0);
        path_dist.assign(n, 0);
        pos.assign(50001, vector<int>());

        max_len = 0;
        min_nodes = 1;

        dfs(0, -1, 0, 0, 0, 0);

        return {(int)max_len, min_nodes};
    }
};
# @lc code=end