#
# @lc app=leetcode id=3534 lang=cpp
#
# [3534] Path Existence Queries in a Graph II
#
# @lc code=start
#include <vector>
#include <queue>
#include <algorithm>
#include <unordered_map>
using namespace std;

class DSU {
public:
    vector<int> parent, rank;
    DSU(int n) : parent(n), rank(n, 0) {
        for (int i = 0; i < n; ++i) parent[i] = i;
    }
    int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }
    void unite(int x, int y) {
        int rx = find(x), ry = find(y);
        if (rx == ry) return;
        if (rank[rx] < rank[ry]) parent[rx] = ry;
        else if (rank[rx] > rank[ry]) parent[ry] = rx;
        else { parent[ry] = rx; rank[rx]++; }
    }
};

class Solution {
public:
    vector<int> pathExistenceQueries(int n, vector<int>& nums, int maxDiff, vector<vector<int>>& queries) {
        vector<int> idx(n);
        for (int i = 0; i < n; ++i) idx[i] = i;
        sort(idx.begin(), idx.end(), [&](int a, int b) { return nums[a] < nums[b]; });
        DSU dsu(n);
        // Build connected components
        for (int i = 0; i + 1 < n; ++i) {
            if (nums[idx[i+1]] - nums[idx[i]] <= maxDiff) {
                dsu.unite(idx[i], idx[i+1]);
            }
        }
        // Build adjacency list for BFS
        vector<vector<int>> adj(n);
        for (int i = 0; i < n; ++i) {
            // For all possible j: |nums[i] - nums[j]| <= maxDiff
            // Since we already connected with DSU, we only need to connect consecutive in sorted order
            if (i > 0 && abs(nums[idx[i]] - nums[idx[i-1]]) <= maxDiff) {
                adj[idx[i]].push_back(idx[i-1]);
            }
            if (i + 1 < n && abs(nums[idx[i]] - nums[idx[i+1]]) <= maxDiff) {
                adj[idx[i]].push_back(idx[i+1]);
            }
        }
        int q = queries.size();
        vector<int> answer(q, -1);
        // Preprocess queries
        unordered_map<int, vector<pair<int, int>>> grouped; // source -> list of (query_idx, target)
        for (int i = 0; i < q; ++i) {
            int u = queries[i][0], v = queries[i][1];
            if (u == v) {
                answer[i] = 0;
            } else if (dsu.find(u) != dsu.find(v)) {
                answer[i] = -1;
            } else {
                grouped[u].emplace_back(i, v);
            }
        }
        // For each group, run BFS from the source to all targets
        for (auto& [src, query_list] : grouped) {
            unordered_map<int, int> targets;
            for (auto& [qi, tgt] : query_list) targets[tgt] = qi;
            vector<int> dist(n, -1);
            queue<int> q;
            dist[src] = 0;
            q.push(src);
            int remain = targets.size();
            while (!q.empty() && remain > 0) {
                int node = q.front(); q.pop();
                if (targets.count(node)) {
                    answer[targets[node]] = dist[node];
                    remain--;
                }
                for (int nei : adj[node]) {
                    if (dist[nei] == -1) {
                        dist[nei] = dist[node] + 1;
                        q.push(nei);
                    }
                }
            }
        }
        return answer;
    }
};
# @lc code=end