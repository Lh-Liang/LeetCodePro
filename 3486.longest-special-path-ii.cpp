#
# @lc app=leetcode id=3486 lang=cpp
#
# [3486] Longest Special Path II
#

# @lc code=start
#include <vector>
#include <algorithm>
#include <set>

using namespace std;

class Solution {
    struct Edge { int to, weight; };
    vector<vector<Edge>> adj;
    vector<int> path_indices[50001];
    vector<long long> prefix_dist;
    multiset<int> ms_dupes;   // Stores first occurrence index of values appearing twice
    multiset<int> ms_triples; // Stores first occurrence index of values appearing thrice
    long long max_len = 0;
    int min_nodes = 0;

    void dfs(int u, int p, long long d, const vector<int>& nums) {
        int val = nums[u];
        int curr_idx = prefix_dist.size();
        prefix_dist.push_back(d + 0); // Placeholder for prefix weight logic
        
        // 1. Remove old state from multisets
        int count = path_indices[val].size();
        if (count == 1) ms_dupes.erase(ms_dupes.find(path_indices[val][0]));
        else if (count == 2) ms_triples.erase(ms_triples.find(path_indices[val][0]));

        // 2. Add current index and update multisets
        path_indices[val].push_back(curr_idx);
        count++;
        if (count == 2) ms_dupes.insert(path_indices[val][0]);
        else if (count == 3) ms_triples.insert(path_indices[val][0]);

        // 3. Calculate path boundary L
        int L = -1;
        if (!ms_triples.empty()) L = max(L, *ms_triples.rbegin());
        if (ms_dupes.size() >= 2) {
            auto it = ms_dupes.rbegin();
            it++; // Get second largest
            L = max(L, *it);
        }

        // 4. Update results
        int start_idx = L + 1;
        long long current_path_len = d - prefix_dist[start_idx];
        int current_path_nodes = curr_idx - start_idx + 1;

        if (current_path_len > max_len) {
            max_len = current_path_len;
            min_nodes = current_path_nodes;
        } else if (current_path_len == max_len) {
            if (min_nodes == 0 || current_path_nodes < min_nodes) min_nodes = current_path_nodes;
        }

        for (auto& edge : adj[u]) {
            if (edge.to != p) dfs(edge.to, u, d + edge.weight, nums);
        }

        // 5. Backtrack
        if (count == 2) ms_dupes.erase(ms_dupes.find(path_indices[val][0]));
        else if (count == 3) ms_triples.erase(ms_triples.find(path_indices[val][0]));
        
        path_indices[val].pop_back();
        count--;
        
        if (count == 1) ms_dupes.insert(path_indices[val][0]);
        else if (count == 2) ms_triples.insert(path_indices[val][0]);
        
        prefix_dist.pop_back();
    }

public:
    vector<int> longestSpecialPath(vector<vector<int>>& edges, vector<int>& nums) {
        int n = nums.size();
        adj.assign(n, {});
        for (auto& e : edges) {
            adj[e[0]].push_back({e[1], e[2]});
            adj[e[1]].push_back({e[0], e[2]});
        }

        max_len = 0; min_nodes = 0;
        prefix_dist.clear();
        // Optimization: only clear used indices if needed, but 5e4 is safe once per call
        for(int i=0; i<=50000; ++i) path_indices[i].clear();
        ms_dupes.clear(); ms_triples.clear();

        dfs(0, -1, 0, nums);
        if (min_nodes == 0) min_nodes = 1; // Single node case
        return {(int)max_len, min_nodes};
    }
};
# @lc code=end